import google.generativeai as genai

from app.config import GEMINI_API_KEY


class CodeGenerationService:


    def __init__(self):

        genai.configure(
            api_key=GEMINI_API_KEY
        )


        self.model = genai.GenerativeModel(
            "gemini-3.5-flash"
        )



    def generate_code(
        self,
        test_cases,
        language
    ):


        prompt = f"""

You are a senior QA automation engineer.

Convert these manual test cases into executable automation code.

Language:
{language}

Requirements:

- Generate clean production quality code
- Use best testing framework
- Add proper assertions
- Add setup and teardown
- No explanations
- Return only code


Test cases:

{test_cases}

"""


        response = (
            self.model.generate_content(
                prompt
            )
        )


        return response.text