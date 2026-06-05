from app.llm_services.base_llm import BaseLLM


class LlamaService(BaseLLM):


    def generate_tests(
        self,
        requirement: str
    ):

        return {

            "model": "Llama",

            "tests": [

                "Check edge cases",

                "Verify boundary conditions",

                "Validate negative scenarios"
            ]
        }