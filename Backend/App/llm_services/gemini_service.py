from app.llm_services.base_llm import BaseLLM


class GeminiService(BaseLLM):


    def generate_tests(
        self,
        requirement: str
    ):

        return {

            "model": "Gemini",

            "tests": [

                "Verify successful user flow",

                "Validate input fields",

                "Check error handling"
            ]
        }