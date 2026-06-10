"""
Test Generation API
TestForge AI

Generates QA test cases using repository context
and user stories.
"""


from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
import logging


from app.agents.test_generation_agent import TestGenerationAgent



# ---------------------------------
# Logger
# ---------------------------------

logger = logging.getLogger(__name__)



# ---------------------------------
# Router
# ---------------------------------

router = APIRouter(
    tags=["Test Generation"]
)



# ---------------------------------
# Agent
# ---------------------------------

test_agent = TestGenerationAgent()





# ---------------------------------
# Request Schema
# ---------------------------------

class TestGenerationRequest(BaseModel):

    repo_context: Dict[str, Any]

    user_story: str

    language: str = "English"





# ---------------------------------
# Generate Test Cases
# ---------------------------------

@router.post(
    "/tests/generate"
)
def generate_test_cases(

    request: TestGenerationRequest

):


    try:


        # Validate story

        if not request.user_story.strip():


            raise HTTPException(

                status_code=400,

                detail="User story is required"

            )





        logger.info(

            "Starting test generation"

        )



        logger.info(

            f"Repository: {request.repo_context.get('project_name')}"

        )







        # Call AI Agent

        result = test_agent.generate_test_cases(


            repo_context=request.repo_context,


            user_story=request.user_story,


            language=request.language


        )







        logger.info(

            "Agent response received"

        )







        # Validate agent result

        if not isinstance(result, dict):


            raise HTTPException(

                status_code=500,

                detail="Invalid response from test generation agent"

            )







        if result.get("status") != "success":



            raise HTTPException(

                status_code=500,


                detail=result.get(

                    "error",

                    "Test generation failed"

                )

            )









        # Return directly to frontend

        return {


            "status":

                "success",



            "message":

                result.get(

                    "message",

                    "Test cases generated successfully"

                ),



            "test_cases":

                result.get(

                    "test_cases",

                    []

                ),




            "summary":

                result.get(

                    "summary",

                    {

                        "total":

                            len(

                                result.get(

                                    "test_cases",

                                    []

                                )

                            )

                    }

                )


        }







    except HTTPException:


        raise








    except Exception as e:



        logger.error(

            f"Test generation error: {str(e)}",

            exc_info=True

        )




        raise HTTPException(

            status_code=500,


            detail=str(e)

        )









# ---------------------------------
# Templates Endpoint
# ---------------------------------

@router.get(
    "/tests/templates"
)
def get_templates():


    return {


        "status":

            "success",



        "message":

            "Templates available",



        "example":

            {


                "id":

                    "TC001",


                "title":

                    "User registration with valid data",



                "description":

                    "Verify user can register successfully",



                "steps":

                    [

                        "Open registration page",

                        "Enter valid details",

                        "Submit form",

                        "Verify account creation"

                    ],



                "expected_result":

                    "User account created successfully",



                "priority":

                    "High",



                "category":

                    "positive"


            }


    }