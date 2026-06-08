from typing import (
    Dict,
    Any,
    Optional
)

from pydantic import BaseModel





class UserStoryRequest(BaseModel):

    user_story: str

    output_type: str = "test_cases"

    language: str

    framework: str

    project_context: Optional[
        Dict[str, Any]
    ] = None

    project_id: int





class UserStoryResponse(BaseModel):

    status: str

    message: str

    story: str

    agent_result: Dict[str, Any]