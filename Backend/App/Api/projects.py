from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.database.models import Project, GenerationHistory
from app.schemas.project_schema import ProjectCreate
from app.security.auth import get_current_user


router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


# CREATE PROJECT

@router.post("/create")
def create_project(
    request: ProjectCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    project = Project(
        name=request.name,
        description=request.description,
        technology=request.technology,
        owner_id=current_user.id
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    return {
        "message": "Project created successfully",
        "project_id": project.id
    }


# GET PROJECTS

@router.get("/")
def get_projects(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return (
        db.query(Project)
        .filter(
            Project.owner_id == current_user.id
        )
        .all()
    )


# UPDATE PROJECT

@router.put("/{project_id}")
def update_project(
    project_id: int,
    request: ProjectCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    project = (
        db.query(Project)
        .filter(
            Project.id == project_id,
            Project.owner_id == current_user.id
        )
        .first()
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    project.name = request.name
    project.description = request.description
    project.technology = request.technology

    db.commit()
    db.refresh(project)

    return {
        "message": "Project updated successfully",
        "project": project
    }


# DELETE PROJECT

@router.delete("/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    project = (
        db.query(Project)
        .filter(
            Project.id == project_id,
            Project.owner_id == current_user.id
        )
        .first()
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    db.delete(project)
    db.commit()

    return {
        "message": "Project deleted successfully"
    }


# PROJECT HISTORY

@router.get("/{project_id}/history")
def project_history(
    project_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return (
        db.query(GenerationHistory)
        .filter(
            GenerationHistory.project_id == project_id,
            GenerationHistory.user_id == current_user.id
        )
        .all()
    )