import google.generativeai as genai

from app.config import settings


class GeminiService:


    def __init__(self):

        genai.configure(
            api_key=settings.GEMINI_API_KEY
        )


        self.model = (
            genai.GenerativeModel(
                "gemini-3.5-flash"
            )
        )


    def generate_tests(
        self,
        requirement
    ):


        prompt = f"""

        You are a senior QA automation engineer.

        Create test scenarios for:

        {requirement}


        Include:
        - Positive test cases
        - Negative test cases
        - Edge cases
        - Security tests


        Return only test points.
        """


        response = (
            self.model
            .generate_content(prompt)
        )


        tests = [
            line.strip()
            for line in response.text.split("\n")
            if line.strip()
        ]


        return {

            "model":
            "Gemini",


            "tests":
            tests
        }
    
    
    def generate_response(
    self,
    prompt
    ):

        try:

            response = (
                self.model
                .generate_content(
                    prompt
                )
            )


            return (
                response.text
            )


        except Exception as e:

            return str(e)