from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.github_service import clone_repository
from app.services.repo_analyzer import analyze_repository


router = APIRouter(
    prefix="/repository",
    tags=["Repository"]
)


class RepoRequest(BaseModel):
    repo_url: str


@router.post("/analyze")
def analyze_repo(request: RepoRequest):

    try:

        path = clone_repository(
            request.repo_url
        )

        result = analyze_repository(
            path
        )

        return {
            "success": True,
            "data": result
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )