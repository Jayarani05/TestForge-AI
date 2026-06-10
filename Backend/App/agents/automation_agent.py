"""
Automation Generation Agent
Converts manual QA test cases into executable automation code.
"""

import json
import logging
import os
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path
from app.core import generate_ai_response

logger = logging.getLogger(__name__)

# Framework detection patterns
FRAMEWORK_PATTERNS = {
    "pytest": {"extensions": [".py"], "keywords": ["pytest", "test_", "requirements.txt"]},
    "junit": {"extensions": [".java"], "keywords": ["junit", "@Test", "maven", "gradle"]},
    "selenium": {"extensions": [".py", ".java", ".js"], "keywords": ["selenium", "WebDriver"]},
    "playwright": {"extensions": [".js", ".ts", ".py"], "keywords": ["playwright", "@playwright"]},
}


class GeneratedTestFile:
    """Represents a generated test automation file"""

    def __init__(
        self,
        filename: str,
        language: str,
        framework: str,
        content: str,
        test_count: int = 0
    ):
        self.filename = filename
        self.language = language
        self.framework = framework
        self.content = content
        self.test_count = test_count
        self.file_path = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "filename": self.filename,
            "language": self.language,
            "framework": self.framework,
            "file_path": self.file_path,
            "test_count": self.test_count,
            "content_length": len(self.content)
        }


class AutomationAgent:
    """
    Automation Generation Agent that converts manual test cases
    into executable automation code.
    """

    def __init__(self):
        """Initialize the automation agent"""
        self.generated_files: List[GeneratedTestFile] = []
        self.output_dir = Path("generated_tests")
        self._ensure_output_dir()
        logger.info("AutomationAgent initialized")

    def _ensure_output_dir(self):
        """Ensure generated_tests directory exists"""
        try:
            self.output_dir.mkdir(parents=True, exist_ok=True)
            logger.info(f"Output directory ensured: {self.output_dir}")
        except Exception as e:
            logger.error(f"Failed to create output directory: {str(e)}")

    def generate_automation(
        self,
        repo_context: Dict[str, Any],
        test_cases: List[Dict[str, Any]],
        project_name: str = "TestProject"
    ) -> Dict[str, Any]:
        """
        Generate automation code from test cases.

        Args:
            repo_context: Repository analysis JSON
            test_cases: List of test cases to automate
            project_name: Name of the project

        Returns:
            Dictionary containing:
                - status: "success" or "error"
                - framework: Detected framework
                - language: Detected language
                - generated_files: List of generated files
                - code: Generated code snippet
                - error: Error message if failed
        """
        try:
            # Detect framework and language
            framework, language = self._detect_framework_and_language(repo_context)

            if not framework:
                return {
                    "status": "error",
                    "message": "Could not detect framework from repository context",
                    "error": "Unsupported or unknown framework"
                }

            logger.info(f"Detected framework: {framework}, language: {language}")

            # Generate automation code using Gemini
            generated_code = self._generate_code_with_gemini(
                framework=framework,
                language=language,
                test_cases=test_cases,
                repo_context=repo_context,
                project_name=project_name
            )

            if not generated_code:
                return {
                    "status": "error",
                    "message": "Failed to generate automation code",
                    "error": "Code generation returned empty result"
                }

            # Save generated files
            file_info = self._save_generated_files(
                framework=framework,
                language=language,
                code=generated_code,
                test_cases=test_cases,
                project_name=project_name
            )

            return {
                "status": "success",
                "message": f"Generated automation code for {len(self.generated_files)} file(s)",
                "framework": framework,
                "language": language,
                "generated_files": [f.to_dict() for f in self.generated_files],
                "code": generated_code[:2000],  # First 2000 chars for preview
                "total_lines": len(generated_code.split("\n")),
                "file_info": file_info
            }

        except Exception as e:
            logger.error(f"Error generating automation: {str(e)}")
            return {
                "status": "error",
                "message": "Failed to generate automation code",
                "error": str(e)
            }

    def _detect_framework_and_language(
        self,
        repo_context: Dict[str, Any]
    ) -> Tuple[Optional[str], Optional[str]]:
        """Detect framework and language from repository context"""
        try:
            framework = repo_context.get("framework", "").lower()
            language = repo_context.get("language", "").lower()
            dependencies = repo_context.get("dependencies", [])
            api_endpoints = repo_context.get("api_endpoints", [])

            # Map framework detection
            if "pytest" in str(dependencies).lower() or framework == "fastapi":
                return "pytest", "python"

            if "junit" in str(dependencies).lower() or language == "java":
                return "junit", "java"

            if "playwright" in str(dependencies).lower() or "playwright" in framework:
                return "playwright", language or "typescript"

            if "selenium" in str(dependencies).lower():
                return "selenium", language or "python"

            if language == "java":
                return "junit", "java"

            if language == "python":
                return "pytest", "python"

            if language in ["javascript", "typescript"]:
                return "playwright", language

            # Default to pytest for Python projects
            if language == "python" or "python" in str(dependencies).lower():
                return "pytest", "python"

            return None, None

        except Exception as e:
            logger.error(f"Error detecting framework: {str(e)}")
            return None, None

    def _generate_code_with_gemini(
        self,
        framework: str,
        language: str,
        test_cases: List[Dict[str, Any]],
        repo_context: Dict[str, Any],
        project_name: str
    ) -> str:
        """Generate automation code using Gemini AI"""
        try:
            # Build prompt based on framework
            prompt = self._build_generation_prompt(
                framework=framework,
                language=language,
                test_cases=test_cases,
                repo_context=repo_context,
                project_name=project_name
            )

            # Generate code using Gemini
            code = generate_ai_response(
                prompt=prompt,
                temperature=0.5,  # Lower temp for more deterministic code
                max_tokens=4000
            )

            return code

        except Exception as e:
            logger.error(f"Error generating code with Gemini: {str(e)}")
            return ""

    def _build_generation_prompt(
        self,
        framework: str,
        language: str,
        test_cases: List[Dict[str, Any]],
        repo_context: Dict[str, Any],
        project_name: str
    ) -> str:
        """Build the prompt for code generation"""

        # Framework-specific instructions
        framework_instructions = self._get_framework_instructions(framework, language)

        test_cases_json = json.dumps(test_cases, indent=2)

        prompt = f"""You are an expert QA automation engineer.

## Task
Convert the following manual QA test cases into executable {framework} automation code using {language}.

## Project Information
- Project Name: {project_name}
- Framework: {framework}
- Language: {language}

## Repository Context
- API Endpoints: {', '.join(repo_context.get('api_endpoints', [])[:5])}
- Dependencies: {', '.join(repo_context.get('dependencies', [])[:5])}

## Framework Instructions
{framework_instructions}

## Test Cases to Automate
{test_cases_json}

## Requirements
1. Generate complete, executable automation code
2. Use proper imports and setup/teardown methods
3. Include descriptive test method names
4. Add assertions for expected results
5. Handle test data and parameterization
6. Include comments explaining test flow
7. Follow {framework} best practices
8. Make tests independent and reusable
9. Include proper error handling
10. Return ONLY executable code with no markdown or explanation

## Code Template
Generate production-ready code that can be run immediately with: {self._get_run_command(framework, language)}

Start generating automation code now:"""

        return prompt

    def _get_framework_instructions(self, framework: str, language: str) -> str:
        """Get framework-specific instructions"""
        instructions = {
            "pytest": """
- Use pytest framework for Python
- Create test functions with test_ prefix
- Use assertions for verification
- Use fixtures for setup/teardown
- Use parametrize for multiple data sets
- Include conftest.py if needed
- Use page object model pattern if testing UI
""",
            "junit": """
- Use JUnit 4 or JUnit 5 framework
- Use @Test annotation for test methods
- Use @Before and @After for setup/teardown
- Use Assert class for verifications
- Use @Parameterized for multiple data sets
- Include proper imports from org.junit
- Use descriptive test method names
""",
            "selenium": """
- Use Selenium WebDriver for browser automation
- Use explicit waits (WebDriverWait) for element handling
- Implement Page Object Model pattern
- Use By selectors to find elements
- Include proper driver initialization and cleanup
- Add try-catch for error handling
- Use appropriate language syntax ({language})
""",
            "playwright": """
- Use Playwright for browser automation
- Use async/await pattern for Playwright
- Implement page object model pattern
- Use page.goto() for navigation
- Use proper selectors and locators
- Include test fixtures and setup/teardown
- Use expect() for assertions
- Proper page.close() and context.close()
"""
        }

        return instructions.get(framework, "")

    def _get_run_command(self, framework: str, language: str) -> str:
        """Get the command to run the tests"""
        commands = {
            "pytest": "pytest test_automation.py",
            "junit": "mvn test or gradle test",
            "selenium": "python test_automation.py or java -cp ... or npm test",
            "playwright": "npx playwright test or pytest test_automation.py"
        }
        return commands.get(framework, "")

    def _save_generated_files(
        self,
        framework: str,
        language: str,
        code: str,
        test_cases: List[Dict[str, Any]],
        project_name: str
    ) -> Dict[str, Any]:
        """Save generated files to disk"""
        try:
            # Determine file extension
            ext_map = {
                "pytest": ".py",
                "junit": ".java",
                "selenium": ".py" if language == "python" else ".java",
                "playwright": ".py" if language == "python" else ".ts"
            }
            extension = ext_map.get(framework, ".py")

            # Create filename
            filename = f"test_{project_name.lower().replace(' ', '_')}_automation{extension}"
            file_path = self.output_dir / filename

            # Write code to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(code)

            # Create GeneratedTestFile object
            generated_file = GeneratedTestFile(
                filename=filename,
                language=language,
                framework=framework,
                content=code,
                test_count=len(test_cases)
            )
            generated_file.file_path = str(file_path)
            self.generated_files.append(generated_file)

            logger.info(f"Generated file saved: {file_path}")

            # Also create a metadata file
            metadata = {
                "project": project_name,
                "framework": framework,
                "language": language,
                "generated_at": str(Path(file_path).stat().st_mtime),
                "test_count": len(test_cases),
                "file": filename
            }

            metadata_file = self.output_dir / f"{filename}.metadata.json"
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2)

            return {
                "saved_file": str(file_path),
                "metadata_file": str(metadata_file),
                "total_tests": len(test_cases),
                "code_lines": len(code.split("\n"))
            }

        except Exception as e:
            logger.error(f"Error saving generated files: {str(e)}")
            return {"error": str(e)}

    def get_generated_files(self) -> List[Dict[str, Any]]:
        """Get list of all generated files"""
        return [f.to_dict() for f in self.generated_files]

    def clear_generated_files(self):
        """Clear generated files list"""
        self.generated_files = []
