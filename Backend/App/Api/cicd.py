from fastapi import APIRouter

from pydantic import BaseModel


from app.agents.cicd_agent import (
    CICDAgent
)



router = APIRouter(
    prefix="/cicd",
    tags=["CI/CD"]
)



class CICDRequest(
    BaseModel
):

    language: str

    framework: str

    tool: str




@router.post(
    "/generate"
)

def generate_pipeline(
    request: CICDRequest
):


    agent = CICDAgent()


    result = agent.generate(

        request.framework,

        request.language,

        request.tool

    )


    return {

        "status":
        "success",


        "pipeline":
        result

    }