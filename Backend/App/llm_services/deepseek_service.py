from app.llm_services.base_llm import BaseLLM


class DeepSeekService(BaseLLM):


    def generate_tests(
        self,
        requirement: str
    ):

        return {

            "model": "DeepSeek",

            "tests": [

                "Security validation",

                "Unauthorized access testing",

                "Failure scenario analysis"
            ]
        }