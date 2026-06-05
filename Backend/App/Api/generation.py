from fastapi import APIRouter

from app.schemas.story_schema import (
    UserStoryRequest,
    UserStoryResponse
)


router = APIRouter(
    prefix="/tests",
    tags=["Test Generation"]
)


@router.post(
    "/generate",
    response_model=UserStoryResponse
)
def generate_tests(
    request: UserStoryRequest
):

   return {
    "status": "success",
    "message": "Story received",
    "story": request.user_story
}