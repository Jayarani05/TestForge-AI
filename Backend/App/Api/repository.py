from fastapi import (
    APIRouter,
    HTTPException,
    Depends
)
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.services.github_service import clone_repository
from app.services.repo_analyzer import analyze_repository
from app.security.auth import get_current_user
from app.database.session import get_db
from app.database.models import Project, RepositoryAnalysis


router = APIRouter(
    prefix="/repository",
    tags=["Repository"]
)


class RepoRequest(BaseModel):
    repo_url: str
    project_id: int = None  # Optional: associate with existing project


@router.post("/analyze")
def analyze_repo(
    request: RepoRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """
    Analyze a GitHub repository.
    
    Request:
    {
        "repo_url": "https://github.com/user/repo",
        "project_id": 1 (optional)
    }
    
    Response:
    {
        "project_name": "repo-name",
        "language": "Python",
        "framework": "FastAPI",
        "total_files": 45,
        "structure": [...],
        "status": "success"
    }
    """
    
    try:
        # Validate URL
        if not request.repo_url:
            raise HTTPException(
                status_code=400,
                detail="Repository URL is required"
            )
        
        # If project_id provided, verify ownership
        if request.project_id:
            project = (
                db.query(Project)
                .filter(
                    Project.id == request.project_id,
                    Project.owner_id == current_user.id
                )
                .first()
            )
            
            if not project:
                raise HTTPException(
                    status_code=404,
                    detail="Project not found or unauthorized"
                )
        
        # Clone repository
        repo_path = clone_repository(request.repo_url)
        
        # Analyze repository
        result = analyze_repository(repo_path)
        
        # Save analysis to database if project_id provided
        if request.project_id:
            analysis_record = RepositoryAnalysis(
                user_id=current_user.id,
                project_id=request.project_id,
                repo_url=request.repo_url,
                analysis_result=result
            )
            db.add(analysis_record)
            db.commit()
        
        return result
    
    except HTTPException:
        raise
    
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to analyze repository: {str(e)}"
        )