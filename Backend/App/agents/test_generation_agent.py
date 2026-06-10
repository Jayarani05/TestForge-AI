"""
Test Case Generation Agent
Generates manual QA test cases based on repository context and user stories.
"""

import json
import logging
from typing import Dict, List, Any, Optional
from app.core import generate_ai_response

logger = logging.getLogger(__name__)


class TestCase:
    """Represents a single test case"""

    def __init__(
        self,
        test_id: str,
        title: str,
        description: str,
        steps: List[str],
        expected_result: str,
        priority: str,
        category: str = "manual"
    ):
        self.id = test_id
        self.title = title
        self.description = description
        self.steps = steps
        self.expected_result = expected_result
        self.priority = priority
        self.category = category

    def to_dict(self) -> Dict[str, Any]:
        """Convert test case to dictionary"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "steps": self.steps,
            "expected_result": self.expected_result,
            "priority": self.priority,
            "category": self.category
        }


class TestGenerationAgent:
    """
    QA Test Generation Agent that creates comprehensive test cases
    from repository context and user stories using Gemini AI.
    """

    def __init__(self):
        """Initialize the test generation agent"""
        self.generated_test_count = 0
        logger.info("TestGenerationAgent initialized")

    def generate_test_cases(
        self,
        repo_context: Dict[str, Any],
        user_story: str,
        language: str = "English"
    ) -> Dict[str, Any]:
        """
        Generate test cases from repository context and user story.

        Args:
            repo_context: Repository analysis JSON with structure, dependencies, etc.
            user_story: User story describing the feature/requirement
            language: Language for test case generation (default: English)

        Returns:
            Dictionary containing:
                - status: "success" or "error"
                - test_cases: List of generated test cases
                - summary: Generation summary with counts
                - error: Error message if failed
        """
        try:
            # Extract repository info for context
            repo_info = self._extract_repo_info(repo_context)

            # Generate prompt for Gemini
            prompt = self._build_test_generation_prompt(
                repo_info=repo_info,
                user_story=user_story,
                language=language
            )

            # Call Gemini to generate test cases
            ai_response = generate_ai_response(
                prompt=prompt,
                temperature=0.7,
                max_tokens=4000
            )

            # Parse AI response into structured test cases
            test_cases = self._parse_test_cases(ai_response)

            if not test_cases:
                return {
                    "status": "error",
                    "message": "Failed to generate test cases",
                    "error": "No valid test cases could be parsed from AI response"
                }

            # Categorize and prioritize test cases
            categorized = self._categorize_test_cases(test_cases)

            self.generated_test_count = len(test_cases)

            return {
                "status": "success",
                "message": f"Generated {len(test_cases)} test cases",
                "test_cases": [tc.to_dict() for tc in test_cases],
                "summary": {
                    "total": len(test_cases),
                    "positive": len(categorized.get("positive", [])),
                    "negative": len(categorized.get("negative", [])),
                    "edge_cases": len(categorized.get("edge_cases", [])),
                    "categories": categorized
                }
            }

        except Exception as e:
            logger.error(f"Error generating test cases: {str(e)}")
            return {
                "status": "error",
                "message": "Failed to generate test cases",
                "error": str(e)
            }

    def _extract_repo_info(self, repo_context: Dict[str, Any]) -> str:
        """Extract key repository information for context"""
        try:
            info_parts = []

            if isinstance(repo_context, dict):
                # Extract useful context from repository analysis
                if "project_name" in repo_context:
                    info_parts.append(f"Project: {repo_context['project_name']}")

                if "language" in repo_context:
                    info_parts.append(f"Language: {repo_context['language']}")

                if "framework" in repo_context:
                    info_parts.append(f"Framework: {repo_context['framework']}")

                if "api_endpoints" in repo_context:
                    endpoints = repo_context["api_endpoints"]
                    if endpoints:
                        info_parts.append(
                            f"API Endpoints: {', '.join(endpoints[:5])}"
                        )

                if "dependencies" in repo_context:
                    deps = repo_context["dependencies"]
                    if deps:
                        info_parts.append(
                            f"Key Dependencies: {', '.join(deps[:5])}"
                        )

            return "\n".join(info_parts) if info_parts else "Project context available"

        except Exception as e:
            logger.warning(f"Error extracting repo info: {str(e)}")
            return "Project context available"

    def _build_test_generation_prompt(
        self,
        repo_info: str,
        user_story: str,
        language: str
    ) -> str:
        """Build the prompt for test case generation"""

        prompt = f"""You are an experienced QA engineer. Your task is to generate comprehensive manual test cases for the following user story.

## Repository Context
{repo_info}

## User Story
{user_story}

## Requirements
Generate ONLY manual QA test cases (NO code generation).
Create test cases in three categories:
1. **Positive Test Cases**: Valid inputs that should work correctly
2. **Negative Test Cases**: Invalid inputs and error scenarios
3. **Edge Cases**: Boundary conditions and special scenarios

## Test Case Format
Return ONLY a valid JSON array with this exact structure. NO additional text before or after the JSON.

[
  {{
    "id": "TC001",
    "title": "Test case title",
    "description": "Detailed description of what is being tested",
    "steps": [
      "Step 1: Action to perform",
      "Step 2: Another action",
      "Step 3: Verification step"
    ],
    "expected_result": "What should happen if the test passes",
    "priority": "High|Medium|Low",
    "category": "positive|negative|edge_case"
  }}
]

## Instructions
1. Generate 3-5 test cases per category (at least 9 total)
2. Each test case must have clear, actionable steps
3. Priority should be based on business impact (High/Medium/Low)
4. Use descriptive titles and clear expected results
5. Return ONLY valid JSON array - no markdown, no code blocks, no additional text
6. Ensure all test case IDs are unique (TC001, TC002, etc.)
7. Cover different user roles and permissions if applicable
8. Include data validation scenarios
9. Include integration points and dependencies

Start generating test cases now. Return ONLY the JSON array:"""

        return prompt

    def _parse_test_cases(self, ai_response: str) -> List[TestCase]:
        """Parse AI response into TestCase objects"""
        try:
            # Try to extract JSON from response
            json_str = ai_response.strip()

            # Remove markdown code blocks if present
            if json_str.startswith("```json"):
                json_str = json_str[7:]
            if json_str.startswith("```"):
                json_str = json_str[3:]
            if json_str.endswith("```"):
                json_str = json_str[:-3]

            json_str = json_str.strip()

            # Parse JSON
            test_data = json.loads(json_str)

            if not isinstance(test_data, list):
                test_data = [test_data]

            test_cases = []
            for item in test_data:
                try:
                    test_case = TestCase(
                        test_id=str(item.get("id", f"TC{len(test_cases)+1:03d}")),
                        title=str(item.get("title", "Untitled Test Case")),
                        description=str(item.get("description", "")),
                        steps=self._ensure_list(item.get("steps", [])),
                        expected_result=str(item.get("expected_result", "")),
                        priority=str(item.get("priority", "Medium")).capitalize(),
                        category=str(item.get("category", "manual"))
                    )
                    test_cases.append(test_case)
                except Exception as e:
                    logger.warning(f"Error parsing individual test case: {str(e)}")
                    continue

            return test_cases

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON from AI response: {str(e)}")
            logger.debug(f"AI Response: {ai_response[:500]}")
            return []
        except Exception as e:
            logger.error(f"Error parsing test cases: {str(e)}")
            return []

    def _ensure_list(self, value: Any) -> List[str]:
        """Ensure value is a list of strings"""
        if isinstance(value, list):
            return [str(v) for v in value]
        elif isinstance(value, str):
            # Try to parse as JSON list first
            try:
                parsed = json.loads(value)
                if isinstance(parsed, list):
                    return [str(v) for v in parsed]
            except:
                pass
            # Split by newlines if it looks like multiple steps
            if "\n" in value:
                return [v.strip() for v in value.split("\n") if v.strip()]
            return [value] if value else []
        return []

    def _categorize_test_cases(
        self,
        test_cases: List[TestCase]
    ) -> Dict[str, List[Dict[str, Any]]]:
        """Categorize test cases by type"""
        categories = {
            "positive": [],
            "negative": [],
            "edge_cases": [],
            "manual": []
        }

        for tc in test_cases:
            category = tc.category.lower()
            if category in categories:
                categories[category].append(tc.to_dict())
            else:
                categories["manual"].append(tc.to_dict())

        return categories

    def validate_test_cases(self, test_cases: List[Dict[str, Any]]) -> bool:
        """Validate that test cases have all required fields"""
        required_fields = {"id", "title", "description", "steps", "expected_result", "priority"}

        for tc in test_cases:
            if not isinstance(tc, dict):
                return False
            if not all(field in tc for field in required_fields):
                return False
            if not isinstance(tc.get("steps"), list):
                return False

        return True
