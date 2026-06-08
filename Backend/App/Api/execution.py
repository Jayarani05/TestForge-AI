from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.test_execution_agent import (
    TestExecutionAgent
)

from app.agents.bug_analyzer_agent import (
    BugAnalyzerAgent
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

    executor = TestExecutionAgent()


    execution_result = executor.execute(
        request.code
    )


    bug_agent = BugAnalyzerAgent()


    bug_report = bug_agent.analyze(
        execution_result
    )


    return {


        "status":
        "success",


        "execution_result":
        execution_result,


        "bug_analysis":
        bug_report

    }