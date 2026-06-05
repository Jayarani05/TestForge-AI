from pydantic import BaseModel


class UserStoryRequest(BaseModel):
    user_story: str


class UserStoryResponse(BaseModel):
    status: str
    message: str
    story: str