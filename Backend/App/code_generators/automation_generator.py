from app.llm_services.code_generation_service import (
    CodeGenerationService
)


class AutomationGenerator:


    def __init__(self):

        self.code_service = (
            CodeGenerationService()
        )



    def generate(
        self,
        test_cases,
        language,
        framework,
        context=None
    ):


        generated_code = (

            self.code_service
            .generate_code(

                test_cases,

                language,

                framework,

                context


            )

        )


        return generated_code