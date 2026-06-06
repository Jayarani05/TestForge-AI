class OutputAgent:


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


            return {


                "type":
                "automation_code",


                "language":
                language,


                "message":
                f"{language} automation generation started"

            }




        return {

            "error":
            "Invalid output type"

        }