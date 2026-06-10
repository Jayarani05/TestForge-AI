"""
Automation Generation API
FastAPI endpoint for generating executable test automation code.
"""

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from typing import Dict, Any, List, Optional
import logging

from app.agents.automation_agent import AutomationAgent
from app.database.session import get_db
from app.security.auth import get_current_user
from app.database.models import User

logger = logging.getLogger(__name__)

# Pydantic Models
class AutomationGenerationRequest(BaseModel):
    """Request schema for automation code generation"""
    repo_context: Dict[str, Any] = Field(
        ...,
        description="Repository analysis JSON containing framework, language, dependencies"
    )
    test_cases: List[Dict[str, Any]] = Field(
        ...,
        description="List of manual test cases to convert to automation code"
    )
    project_name: Optional[str] = Field(
        "TestProject",
        description="Name of the project for file naming"
    )
    project_id: Optional[int] = Field(
        None,
        description="Optional project ID for association"
    )


class GeneratedFileInfo(BaseModel):
    """Info about a generated file"""
    filename: str
    language: str
    framework: str
    file_path: Optional[str] = None
    test_count: int
    content_length: int


class AutomationGenerationResponse(BaseModel):
    """Response schema for automation generation"""
    status: str
    message: str
    framework: Optional[str] = None
    language: Optional[str] = None
    generated_files: List[GeneratedFileInfo] = []
    code: Optional[str] = None
    total_lines: Optional[int] = None
    file_info: Optional[Dict[str, Any]] = None
    error: Optional[str] = None


# Initialize router
router = APIRouter(
    tags=["Automation Generation"]
)

# Initialize agent
automation_agent = AutomationAgent()


@router.post(
    "/automation/generate",
    response_model=AutomationGenerationResponse
)
def generate_automation(
    request: AutomationGenerationRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Generate executable test automation code from manual test cases.

    **Request Body:**
    - `repo_context`: Repository analysis JSON with framework, language, dependencies
    - `test_cases`: List of manual test cases to automate
    - `project_name`: (Optional) Project name for file naming
    - `project_id`: (Optional) Project ID for association

    **Response:**
    Returns generated automation code with:
    - Framework: Detected or specified framework (pytest, junit, selenium, playwright)
    - Language: Programming language (python, java, javascript, typescript)
    - Generated files: List of created automation test files
    - Code: Preview of generated code (first 2000 chars)

    **Supported Frameworks:**
    - Python: pytest
    - Java: JUnit
    - Frontend: Selenium / Playwright
    """
    try:
        # Validate inputs
        if not request.repo_context:
            raise HTTPException(
                status_code=400,
                detail="repo_context is required"
            )

        if not request.test_cases or len(request.test_cases) == 0:
            raise HTTPException(
                status_code=400,
                detail="test_cases cannot be empty"
            )

        logger.info(
            f"Generating automation code for user {current_user.id} "
            f"with {len(request.test_cases)} test cases"
        )

        # Generate automation code
        result = automation_agent.generate_automation(
            repo_context=request.repo_context,
            test_cases=request.test_cases,
            project_name=request.project_name
        )

        # Check if generation was successful
        if result.get("status") != "success":
            logger.warning(f"Automation generation failed: {result.get('error')}")
            raise HTTPException(
                status_code=500,
                detail=result.get("error", "Failed to generate automation code")
            )

        # Log success
        logger.info(
            f"Successfully generated automation code "
            f"for framework: {result.get('framework')}, "
            f"language: {result.get('language')}"
        )

        # Prepare response
        response = AutomationGenerationResponse(
            status="success",
            message=result.get("message"),
            framework=result.get("framework"),
            language=result.get("language"),
            generated_files=result.get("generated_files", []),
            code=result.get("code"),
            total_lines=result.get("total_lines"),
            file_info=result.get("file_info")
        )

        return response

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in automation generation endpoint: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Failed to generate automation code due to an internal error"
        )


@router.get(
    "/automation/frameworks"
)
def get_supported_frameworks():
    """
    Get list of supported automation frameworks and their details.

    Returns:
        List of supported frameworks with language, detection keywords, and examples
    """
    return {
        "status": "success",
        "supported_frameworks": [
            {
                "name": "pytest",
                "language": "python",
                "description": "Python testing framework with fixtures and parametrization",
                "run_command": "pytest test_automation.py",
                "best_for": "Backend API testing, unit testing"
            },
            {
                "name": "junit",
                "language": "java",
                "description": "Java testing framework with annotations",
                "run_command": "mvn test or gradle test",
                "best_for": "Java backend applications, microservices"
            },
            {
                "name": "selenium",
                "language": "python, java, javascript",
                "description": "Browser automation for web applications",
                "run_command": "python test_automation.py",
                "best_for": "Web UI testing, cross-browser testing"
            },
            {
                "name": "playwright",
                "language": "javascript, typescript, python",
                "description": "Modern browser automation with async support",
                "run_command": "npx playwright test",
                "best_for": "Modern web applications, performance testing"
            }
        ]
    }


@router.get(
    "/automation/examples/{framework}"
)
def get_framework_examples(framework: str):
    """
    Get code examples for a specific automation framework.

    Args:
        framework: Framework name (pytest, junit, selenium, playwright)

    Returns:
        Code examples and best practices for the framework
    """
    examples = {
        "pytest": {
            "description": "Python pytest framework example",
            "code": """import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLoginFeature:
    \"\"\"Test cases for login functionality\"\"\"

    @pytest.fixture(autouse=True)
    def setup(self):
        \"\"\"Setup before each test\"\"\"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    def test_login_with_valid_credentials(self):
        \"\"\"Test successful login with valid credentials\"\"\"
        self.driver.get("http://localhost:5173/login")
        
        # Find and fill login form
        email_field = self.driver.find_element(By.ID, "email")
        password_field = self.driver.find_element(By.ID, "password")
        
        email_field.send_keys("user@example.com")
        password_field.send_keys("correct_password")
        
        # Submit form
        login_button = self.driver.find_element(By.ID, "login_btn")
        login_button.click()
        
        # Verify redirect
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/dashboard")
        )
        assert "/dashboard" in self.driver.current_url
"""
        },
        "junit": {
            "description": "Java JUnit framework example",
            "code": """import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.AfterEach;
import static org.junit.jupiter.api.Assertions.*;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.By;


public class TestLoginFeature {
    private WebDriver driver;

    @BeforeEach
    public void setUp() {
        // Initialize WebDriver
        System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver");
        driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
    }

    @Test
    public void testLoginWithValidCredentials() {
        driver.get("http://localhost:5173/login");
        
        WebElement emailField = driver.findElement(By.id("email"));
        WebElement passwordField = driver.findElement(By.id("password"));
        WebElement loginButton = driver.findElement(By.id("login_btn"));
        
        emailField.sendKeys("user@example.com");
        passwordField.sendKeys("correct_password");
        loginButton.click();
        
        WebDriverWait wait = new WebDriverWait(driver, 10);
        wait.until(ExpectedConditions.urlContains("/dashboard"));
        
        assertTrue(driver.getCurrentUrl().contains("/dashboard"));
    }

    @AfterEach
    public void tearDown() {
        driver.quit();
    }
}
"""
        },
        "playwright": {
            "description": "Playwright JavaScript example",
            "code": """import { test, expect } from '@playwright/test';

test.describe('Login Feature Tests', () => {
    let page;

    test.beforeEach(async ({ browser }) => {
        const context = await browser.newContext();
        page = await context.newPage();
    });

    test('Login with valid credentials', async () => {
        await page.goto('http://localhost:5173/login');
        
        await page.fill('#email', 'user@example.com');
        await page.fill('#password', 'correct_password');
        await page.click('#login_btn');
        
        await page.waitForURL('**/dashboard');
        expect(page.url()).toContain('/dashboard');
    });

    test('Login with invalid credentials', async () => {
        await page.goto('http://localhost:5173/login');
        
        await page.fill('#email', 'user@example.com');
        await page.fill('#password', 'wrong_password');
        await page.click('#login_btn');
        
        const errorMsg = await page.locator('.error-message').textContent();
        expect(errorMsg).toContain('Invalid credentials');
    });
});
"""
        },
        "selenium": {
            "description": "Selenium WebDriver example",
            "code": """from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestLoginFeature:
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def test_login_with_valid_credentials(self):
        self.driver.get("http://localhost:5173/login")
        
        email_field = self.driver.find_element(By.ID, "email")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login_btn")
        
        email_field.send_keys("user@example.com")
        password_field.send_keys("correct_password")
        login_button.click()
        
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/dashboard")
        )
        
        assert "/dashboard" in self.driver.current_url
        
    def teardown(self):
        self.driver.quit()
"""
        }
    }

    if framework.lower() not in examples:
        raise HTTPException(
            status_code=404,
            detail=f"Framework '{framework}' not found"
        )

    return {
        "status": "success",
        "framework": framework,
        "example": examples[framework.lower()]
    }


@router.get(
    "/automation/generated-files"
)
def list_generated_files():
    """
    List all generated automation files.

    Returns:
        List of generated files with metadata
    """
    try:
        files = automation_agent.get_generated_files()
        return {
            "status": "success",
            "total_files": len(files),
            "files": files
        }
    except Exception as e:
        logger.error(f"Error listing generated files: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Failed to list generated files"
        )
