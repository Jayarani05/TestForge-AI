from pydantic import BaseModel
from typing import Dict, Any


class UserStoryRequest(BaseModel):
    user_story: str


class UserStoryResponse(BaseModel):
    status: str
    message: str
    story: str
    agent_result: Dict[str, Any]