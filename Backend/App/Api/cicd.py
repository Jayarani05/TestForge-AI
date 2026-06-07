from fastapi import APIRouter

from pydantic import BaseModel


from app.agents.cicd_agent import CICDAgent




router = APIRouter(

    prefix="/cicd",

    tags=["CI/CD"]

)



agent = CICDAgent()





class CICDRequest(BaseModel):

    project_type:str

    framework:str

    tool:str

    requirement:str







@router.post("/generate")


def generate_pipeline(

    request:CICDRequest

):



    result = agent.generate(


        language=request.project_type,

        framework=request.framework,

        tool=request.tool


    )




    return {

        "status":"success",


        "project_type":

        request.project_type,


        "framework":

        request.framework,


        "tool":

        request.tool,


        "pipeline_code":

        result

    }
