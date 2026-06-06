from app.code_generators.automation_generator import (
    AutomationGenerator
)


class OutputAgent:

    def __init__(
        self
    ):


        self.automation_generator = (
            AutomationGenerator()
        )


    def generate(
        self,
        output_type,
        test_cases,
        language=None
    ):



        if output_type == "test_cases":


            return {


                "type":
                "manual_test_cases",


                "result":
                test_cases

            }





        if output_type == "automation":


            code = (

                self.automation_generator
                .generate(

                    test_cases,

                    language

                )

            )



            return {


                "type":
                "automation_code",


                "language":
                language,


                "code":
                code

            }




        return {

            "error":
            "Invalid output type"

        }