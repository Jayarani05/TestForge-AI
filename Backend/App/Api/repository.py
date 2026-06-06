from fastapi import APIRouter

from pydantic import BaseModel


from app.agents.repository_agent import (
    RepositoryAgent
)



router = APIRouter(
    prefix="/repository",
    tags=["Repository Intelligence"]
)



class RepoRequest(
    BaseModel
):

    repo_url: str




@router.post(
    "/analyze"
)

def analyze_repository(
    request: RepoRequest
):


    agent = RepositoryAgent()


    result = agent.analyze(
        request.repo_url
    )


    return {


        "status":
        "success",


        "repository_analysis":
        result

    }