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
        language,
        framework
    ):


        prompt = f"""

You are a senior QA automation engineer.

Generate automation code.

Programming Language:
{language}

Testing Framework:
{framework}

Rules:

- Strictly use the selected framework only
- Do not switch frameworks
- Add setup
- Add teardown
- Add assertions
- Return only executable code

Test cases:

{test_cases}

"""


        response = (
            self.model.generate_content(
                prompt
            )
        )


        return response.text