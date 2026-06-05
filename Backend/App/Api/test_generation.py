from fastapi import APIRouter

from app.schemas.story_schema import (
    UserStoryRequest,
    TestGenerationResponse
)


router = APIRouter(
    prefix="/tests",
    tags=["Test Generation"]
)


@router.post(
    "/generate",
    response_model=TestGenerationResponse
)
def generate_tests(
    request: UserStoryRequest
):

    return {
        "status": "success",

        "message": "User story received successfully",

        "received_story": request.user_story
    }