"""
Test Generation API
FastAPI endpoint for generating test cases from repository context and user stories.
"""

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from typing import Dict, Any, List, Optional
import logging

from app.agents.test_generation_agent import TestGenerationAgent
from app.database.session import get_db
from app.security.auth import get_current_user
from app.database.models import Project, User

logger = logging.getLogger(__name__)

# Pydantic Models
class TestCaseStep(BaseModel):
    """Individual test step"""
    pass


class TestCaseSchema(BaseModel):
    """Test case schema"""
    id: str
    title: str
    description: str
    steps: List[str]
    expected_result: str
    priority: str
    category: Optional[str] = "manual"


class TestGenerationRequest(BaseModel):
    """Request schema for test case generation"""
    repo_context: Dict[str, Any] = Field(
        ...,
        description="Repository analysis JSON containing project structure, dependencies, etc."
    )
    user_story: str = Field(
        ...,
        description="User story describing the feature to test"
    )
    project_id: Optional[int] = Field(
        None,
        description="Optional project ID to associate with generated test cases"
    )
    language: str = Field(
        "English",
        description="Language for test case generation"
    )


class TestCaseSummary(BaseModel):
    """Summary of generated test cases"""
    total: int
    positive: int
    negative: int
    edge_cases: int


class TestGenerationResponse(BaseModel):
    """Response schema for test case generation"""
    status: str
    message: str
    test_cases: List[TestCaseSchema]
    summary: Optional[Dict[str, Any]] = None
    error: Optional[str] = None


# Initialize router
router = APIRouter(
    tags=["Test Generation"]
)

# Initialize agent
test_generation_agent = TestGenerationAgent()


@router.post(
    "/tests/generate",
    response_model=TestGenerationResponse
)
def generate_test_cases(
    request: TestGenerationRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Generate manual QA test cases from repository context and user story.

    **Request Body:**
    - `repo_context`: Repository analysis JSON from repository analyzer
    - `user_story`: User story or feature description to generate tests for
    - `project_id`: (Optional) Project ID to associate with test cases
    - `language`: (Optional) Language for generation (default: English)

    **Response:**
    Returns generated test cases categorized into:
    - Positive scenarios: Valid inputs that should work
    - Negative scenarios: Invalid inputs and error cases
    - Edge cases: Boundary conditions and special scenarios

    Each test case includes:
    - id: Unique test case identifier
    - title: Test case title
    - description: Detailed description
    - steps: List of test steps
    - expected_result: Expected outcome
    - priority: Test priority (High/Medium/Low)
    - category: Test category (positive/negative/edge_case)
    """
    try:
        # Validate repo_context is provided
        if not request.repo_context:
            raise HTTPException(
                status_code=400,
                detail="repo_context is required"
            )

        # Validate user_story is not empty
        if not request.user_story or not request.user_story.strip():
            raise HTTPException(
                status_code=400,
                detail="user_story cannot be empty"
            )

        # Verify project ownership if project_id is provided
        if request.project_id:
            project = db.query(Project).filter(
                Project.id == request.project_id,
                Project.owner_id == current_user.id
            ).first()

            if not project:
                raise HTTPException(
                    status_code=404,
                    detail="Project not found or access denied"
                )

        logger.info(
            f"Generating test cases for user {current_user.id} "
            f"with story: {request.user_story[:50]}..."
        )

        # Generate test cases using agent
        result = test_generation_agent.generate_test_cases(
            repo_context=request.repo_context,
            user_story=request.user_story,
            language=request.language
        )

        # Check if generation was successful
        if result.get("status") != "success":
            logger.warning(f"Test generation failed: {result.get('error')}")
            raise HTTPException(
                status_code=500,
                detail=result.get("error", "Failed to generate test cases")
            )

        # Log success
        test_count = len(result.get("test_cases", []))
        logger.info(f"Successfully generated {test_count} test cases")

        # Prepare response
        response = TestGenerationResponse(
            status="success",
            message=result.get("message", "Test cases generated successfully"),
            test_cases=result.get("test_cases", []),
            summary=result.get("summary")
        )

        return response

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in test generation endpoint: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Failed to generate test cases due to an internal error"
        )


@router.get(
    "/tests/templates"
)
def get_test_templates():
    """
    Get available test case templates and examples.

    Returns example test case structure and generation guidelines.
    """
    return {
        "status": "success",
        "templates": {
            "positive_scenario": {
                "id": "TC001",
                "title": "Valid user login with correct credentials",
                "description": "Test that a user can successfully login with valid email and password",
                "steps": [
                    "Navigate to login page",
                    "Enter valid email address",
                    "Enter correct password",
                    "Click login button",
                    "Verify redirect to dashboard"
                ],
                "expected_result": "User is logged in and redirected to dashboard",
                "priority": "High",
                "category": "positive"
            },
            "negative_scenario": {
                "id": "TC002",
                "title": "User login with incorrect password",
                "description": "Test that login fails with incorrect password",
                "steps": [
                    "Navigate to login page",
                    "Enter valid email address",
                    "Enter incorrect password",
                    "Click login button",
                    "Verify error message is displayed"
                ],
                "expected_result": "Error message shown, user remains on login page",
                "priority": "High",
                "category": "negative"
            },
            "edge_case": {
                "id": "TC003",
                "title": "Login with special characters in password",
                "description": "Test login with complex password containing special characters",
                "steps": [
                    "Navigate to login page",
                    "Enter valid email",
                    "Enter password with special characters (!@#$%^)",
                    "Click login button",
                    "Verify successful login"
                ],
                "expected_result": "User logs in successfully with special character password",
                "priority": "Medium",
                "category": "edge_case"
            }
        }
    }
