from app.llm_services.gemini_service import GeminiService
from app.llm_services.llama_service import LlamaService
from app.llm_services.deepseek_service import DeepSeekService


class MultiLLMOrchestrator:


    def __init__(self):

        self.models = [

            GeminiService(),

            LlamaService(),

            DeepSeekService()
        ]


    def generate_all(
        self,
        requirement
    ):

        responses = []


        for model in self.models:

            responses.append(

                model.generate_tests(
                    requirement
                )

            )


        return responses