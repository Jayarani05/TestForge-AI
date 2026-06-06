from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.test_execution_agent import (
    TestExecutionAgent
)


router = APIRouter(
    prefix="/execution",
    tags=["Execution"]
)


class ExecutionRequest(
    BaseModel
):

    code: str



@router.post(
    "/run"
)

def execute_test(
    request: ExecutionRequest
):

    agent = TestExecutionAgent()


    result = agent.execute(
        request.code
    )


    return {

        "status":
        "success",


        "execution_result":
        result

    }