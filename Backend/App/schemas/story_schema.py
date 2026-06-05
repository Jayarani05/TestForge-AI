from pydantic import BaseModel


class UserStoryRequest(BaseModel):

    user_story: str


class TestGenerationResponse(BaseModel):

    status: str
    message: str
    received_story: str