
from typing import Dict, Any
from typing import Optional
from pydantic import BaseModel



class UserStoryRequest(BaseModel):


    user_story: str


    output_type: str = "test_cases"


    language: Optional[str] = None

    framework: Optional[str] = None

    project_context: Optional[
        Dict[str, Any]
    ] = None


class UserStoryResponse(BaseModel):
    status: str
    message: str
    story: str
    agent_result: Dict[str, Any]