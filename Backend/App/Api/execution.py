from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
import logging

from app.agents.test_execution_agent import (
    TestExecutionAgent
)

from app.agents.bug_analyzer_agent import (
    BugAnalyzerAgent
)

from app.services.executor import TestExecutor
from app.database.session import get_db
from app.security.auth import get_current_user
from app.database.models import User
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)

router = APIRouter(
    tags=["Execution"]
)


class ExecutionRequest(
    BaseModel
):

    code: str


class TestRunRequest(BaseModel):
    """Request schema for running generated tests"""
    test_file_path: str = Field(
        ...,
        description="Path to the test file to run"
    )
    framework: Optional[str] = Field(
        None,
        description="Framework to use (pytest, npm, mvn). Auto-detect if not provided"
    )
    timeout: int = Field(
        300,
        description="Execution timeout in seconds (default 300)"
    )


class TestRunResponse(BaseModel):
    """Response schema for test execution"""
    status: str
    framework: str
    total_tests: int
    passed_tests: int
    failed_tests: int
    skipped_tests: int
    execution_time: float
    logs: str
    errors: str
    success: bool


@router.post(
    "/execution/run"
)

def execute_test(
    request: ExecutionRequest
):

    executor = TestExecutionAgent()


    execution_result = executor.execute(
        request.code
    )


    bug_agent = BugAnalyzerAgent()


    bug_report = bug_agent.analyze(
        execution_result
    )


    return {


        "status":
        "success",


        "execution_result":
        execution_result,


        "bug_analysis":
        bug_report

    }


@router.post(
    "/tests/run",
    response_model=TestRunResponse
)
def run_generated_tests(
    request: TestRunRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Run generated automation tests and capture results.

    **Request Body:**
    - `test_file_path`: Path to the test file to run
    - `framework`: (Optional) Framework (pytest, npm, mvn). Auto-detect if not provided
    - `timeout`: (Optional) Execution timeout in seconds (default 300)

    **Response:**
    Returns test execution results with:
    - status: Execution status (success/failed/timeout/error)
    - framework: Framework used for execution
    - Test counts: total, passed, failed, skipped
    - logs: Complete execution logs
    - errors: Error messages if any
    - execution_time: Total execution time in seconds

    **Supported Frameworks:**
    - pytest: Python testing framework
    - npm test: JavaScript/TypeScript testing
    - mvn test: Maven (Java) testing

    **Auto-Detection:**
    If framework is not provided, it will be auto-detected from:
    - File extension: .py (pytest), .js/.ts (npm), .java (mvn)
    - Directory contents: test_*.py, *.test.js, pom.xml
    """
    try:
        # Validate input
        if not request.test_file_path or not request.test_file_path.strip():
            raise HTTPException(
                status_code=400,
                detail="test_file_path is required"
            )

        if request.timeout < 10:
            raise HTTPException(
                status_code=400,
                detail="timeout must be at least 10 seconds"
            )

        logger.info(
            f"Running tests for user {current_user.id} "
            f"from file: {request.test_file_path}"
        )

        # Initialize test executor
        executor = TestExecutor()

        # Execute tests
        result = executor.execute_test_file(
            file_path=request.test_file_path,
            framework=request.framework,
            timeout=request.timeout
        )

        logger.info(
            f"Test execution completed with status: {result.status}, "
            f"passed: {result.passed_tests}, failed: {result.failed_tests}"
        )

        # Return response
        return TestRunResponse(
            status=result.status,
            framework=result.framework,
            total_tests=result.total_tests,
            passed_tests=result.passed_tests,
            failed_tests=result.failed_tests,
            skipped_tests=result.skipped_tests,
            execution_time=result.execution_time,
            logs=result.logs,
            errors=result.errors,
            success=result.status == "success"
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error running tests: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Failed to run tests due to an internal error"
        )


@router.get(
    "/tests/frameworks"
)
def get_test_frameworks():
    """
    Get list of supported test frameworks and execution details.

    Returns:
        Information about supported test frameworks and how to use them
    """
    return {
        "status": "success",
        "supported_frameworks": [
            {
                "name": "pytest",
                "language": "Python",
                "description": "Python unittest framework with fixtures and assertions",
                "file_extensions": [".py"],
                "auto_detect_patterns": ["test_*.py", "*_test.py"],
                "install_command": "pip install pytest",
                "example_file": "test_example.py"
            },
            {
                "name": "npm",
                "language": "JavaScript / TypeScript",
                "description": "Node Package Manager test runner (Jest, Mocha, etc.)",
                "file_extensions": [".js", ".ts"],
                "auto_detect_patterns": ["*.test.js", "*.spec.js"],
                "install_command": "npm install --save-dev",
                "example_file": "test_example.js"
            },
            {
                "name": "mvn",
                "language": "Java",
                "description": "Maven test runner for Java applications (JUnit)",
                "file_extensions": [".java"],
                "auto_detect_patterns": ["*Test.java", "pom.xml"],
                "install_command": "Maven must be installed system-wide",
                "example_file": "TestExample.java"
            }
        ]
    }


@router.get(
    "/tests/status/{execution_id}"
)
def get_test_status(execution_id: str):
    """
    Get status of a test execution (for future async support).

    Args:
        execution_id: ID of the execution to check

    Returns:
        Execution status and results
    """
    return {
        "status": "not_implemented",
        "message": "Async test execution status tracking coming soon"
    }
