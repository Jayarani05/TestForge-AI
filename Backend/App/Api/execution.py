from fastapi import APIRouter
from pydantic import BaseModel


from app.agents.test_execution_agent import (
    TestExecutionAgent
)


from app.agents.bug_analyzer_agent import (
    BugAnalyzerAgent
)


from app.agents.self_healing_agent import (
    SelfHealingAgent
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



    # ==========================
    # TEST EXECUTION AGENT
    # ==========================


    executor = TestExecutionAgent()



    execution_result = executor.execute(

        request.code

    )







    # ==========================
    # BUG ANALYZER AGENT
    # ==========================


    bug_agent = BugAnalyzerAgent()



    bug_report = bug_agent.analyze(

        execution_result

    )









    # ==========================
    # SELF HEALING AGENT
    # ==========================


    self_healing = {


        "applied": False,


        "message":

        "No healing required"


    }






    if not execution_result.get(

        "passed"

    ):



        healer = SelfHealingAgent()



        healing_result = healer.heal(


            failed_code=

            request.code,



            error_log=

            execution_result.get(

                "errors",

                execution_result.get(

                    "error",

                    ""

                )

            ),




            dom_snapshot=

            "Runtime DOM snapshot unavailable"


        )





        self_healing = {


            "applied": True,


            "fixed_code":

            healing_result


        }









    return {


        "status":

        "success",



        "execution_result":

        execution_result,



        "bug_analysis":

        bug_report,



        "self_healing":

        self_healing


    }