from openai import OpenAI

from app.config import settings

class DeepSeekService:


    def __init__(self):

        self.client = OpenAI(

            api_key=settings.DEEPSEEK_API_KEY,

            base_url="https://openrouter.ai/api/v1"
        )


    def generate_tests(
        self,
        requirement
    ):


        prompt = f"""

        You are a senior QA automation engineer.

        Generate detailed test scenarios.

        Requirement:

        {requirement}


        Include:

        - Positive test cases
        - Negative test cases
        - Edge cases
        - Security test cases

        Return only test points.
        """


        try:


            response = (

                self.client
                .chat
                .completions
                .create(

                    model="deepseek/deepseek-chat",

                    messages=[

                        {
                            "role": "system",

                            "content":
                            "You are an expert QA and security testing engineer."
                        },


                        {
                            "role": "user",

                            "content": prompt
                        }

                    ],


                    temperature=0.3
                )

            )


            output = (

                response
                .choices[0]
                .message
                .content

            )


            tests = [

                line.strip()

                for line in output.split("\n")

                if line.strip()

            ]


            return {

                "model":
                "DeepSeek",


                "status":
                "success",


                "tests":
                tests

            }



        except Exception as error:


            return {

                "model":
                "DeepSeek",


                "status":
                "failed",


                "error":
                repr(error),


                "tests":
                [

                    "DeepSeek fallback activated"

                ]

            }