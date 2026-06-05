from openai import OpenAI

from app.config import DEEPSEEK_API_KEY


class DeepSeekService:


    def __init__(self):

        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=DEEPSEEK_API_KEY
        )


    def generate_tests(
        self,
        requirement
    ):


        try:

            response = (
                self.client
                .chat
                .completions
                .create(

                    model=
                    "deepseek/deepseek-chat",

                    messages=[
                        {
                            "role":
                            "system",

                            "content":
                            "You are a senior QA security engineer"
                        },


                        {
                            "role":
                            "user",

                            "content":
                            f"""
                            Generate QA test cases:

                            {requirement}

                            Focus on:
                            security testing,
                            edge cases,
                            failures
                            """
                        }
                    ]
                )
            )


            result = (
                response
                .choices[0]
                .message
                .content
            )


            tests = [

                line.strip()

                for line in result.split("\n")

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

                "tests":[
                    "DeepSeek fallback activated"
                ]
            }