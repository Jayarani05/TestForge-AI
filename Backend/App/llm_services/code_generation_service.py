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
        framework,
        context=None
    ):


        prompt = f"""

You are a senior QA automation engineer.

Generate automation code.

Programming Language:
{language}

Testing Framework:
{framework}

Application Context:

{context}

Rules:

- Use provided URL
- Use provided selectors
- Do not create fake HTML
- Do not assume elements
- Generate executable automation

Test cases:

{test_cases}

"""


        response = (
            self.model.generate_content(
                prompt
            )
        )


        return response.text