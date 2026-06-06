from fastapi import APIRouter
from app.agents.qa_agent import QAAgent
from app.schemas.story_schema import (
    UserStoryRequest,
    UserStoryResponse
)


router = APIRouter(
    prefix="/tests",
    tags=["Test Generation"]
)


@router.post(
    "/generate"
)
def generate_tests(
    request: UserStoryRequest
):

    agent = QAAgent()


    result = agent.process_story(
        request.user_story,

        request.output_type,

        request.language

    )


    return {
        "status": "success",

        "message":
        "QA Agent executed successfully",

        "story":
        request.user_story,

        "agent_result":
        result
    }
