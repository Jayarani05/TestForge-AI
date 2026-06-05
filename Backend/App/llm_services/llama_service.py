from groq import Groq

from app.config import GROQ_API_KEY


class LlamaService:


    def __init__(self):

        self.client = Groq(
            api_key=GROQ_API_KEY
        )


    def generate_tests(
        self,
        requirement
    ):


        prompt = f"""

        Act as a senior QA engineer.

        Generate test scenarios.

        Requirement:
        {requirement}

        Include:
        - functional testing
        - negative testing
        - edge cases
        - security testing

        Return only test points.
        """


        try:

            response = (
                self.client.chat.completions.create(

                    model="llama-3.1-8b-instant",

                    messages=[
                        {
                            "role":"user",
                            "content":prompt
                        }
                    ]

                )
            )


            content = (
                response
                .choices[0]
                .message
                .content
            )


            tests = [

                line.strip()

                for line in content.split("\n")

                if line.strip()
            ]


            return {

                "model":
                "Llama",

                "status":
                "success",

                "tests":
                tests
            }


        except Exception as error:


            return {

                "model":
                "Llama",

                "status":
                "failed",

                "error":
                str(error),

                "tests":[
                    "Llama fallback activated"
                ]

            }