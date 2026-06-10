import json
import logging
from typing import Dict, Any

from app.core.gemini_client import generate_ai_response
from google.api_core.exceptions import PermissionDenied, InvalidArgument, GoogleAPIError

logger = logging.getLogger(__name__)



def _get_mock_requirement_analysis(user_story: str) -> Dict[str, Any]:
    """
    Generate mock requirement analysis for testing/fallback.
    Used when API is not available.
    """
    return {
        "functional_requirements": [
            "User should be able to access the feature",
            "System should validate user input",
            "System should return appropriate response"
        ],
        "non_functional_requirements": [
            "Response time < 2 seconds",
            "System uptime > 99.9%",
            "Support 1000+ concurrent users"
        ],
        "sentiment": {
            "type": "neutral",
            "confidence": 0.7,
            "reason": "Story describes functional requirements"
        },
        "risk_analysis": {
            "risk_level": "low",
            "risks": [
                "Incomplete requirements specification",
                "Potential edge cases not covered"
            ]
        }
    }


def analyze_requirement(user_story: str) -> Dict[str, Any]:
    """
    Analyze a user story and extract requirements using Gemini AI.
    Falls back to mock responses if API is unavailable.
    
    Args:
        user_story: The user story to analyze
        
    Returns:
        Dictionary with functional_requirements, non_functional_requirements, sentiment, and risk_analysis
    """
    
    prompt = f"""You are a senior QA requirement analyst.

Analyze this user story:

{user_story}

Return ONLY JSON (no markdown, no code blocks, no additional text):

{{
"functional_requirements": [],
"non_functional_requirements": [],
"sentiment": {{
  "type": "",
  "confidence": 0,
  "reason": ""
}},
"risk_analysis": {{
  "risk_level": "",
  "risks": []
}}
}}"""

    try:
        # Use the centralized Gemini client
        response = generate_ai_response(
            prompt=prompt,
            temperature=0.5,
            max_tokens=1500
        )

        # Clean markdown code blocks if present
        clean_response = response.replace(
            "```json", ""
        ).replace(
            "```", ""
        ).strip()

        # Parse JSON
        try:
            return json.loads(clean_response)
        except json.JSONDecodeError as e:
            logger.warning(f"Failed to parse JSON response: {e}. Using mock response.")
            return _get_mock_requirement_analysis(user_story)
            
    except PermissionDenied as e:
        logger.error(
            f"API Permission Denied: {str(e)}. "
            "Ensure Gemini API is enabled in your Google Cloud project and has proper access. "
            "Using mock response for testing."
        )
        return _get_mock_requirement_analysis(user_story)
        
    except InvalidArgument as e:
        logger.error(f"Invalid API argument: {str(e)}. Using mock response.")
        return _get_mock_requirement_analysis(user_story)
        
    except GoogleAPIError as e:
        logger.error(f"Google API error: {str(e)}. Using mock response.")
        return _get_mock_requirement_analysis(user_story)
        
    except Exception as e:
        logger.error(f"Unexpected error in analyze_requirement: {str(e)}. Using mock response.")
        return _get_mock_requirement_analysis(user_story)