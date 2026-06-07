from groq import Groq

from app.config import settings


class LlamaService:


    def __init__(self):

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )


    def generate_tests(
        self,
        requirement
    ):

        try:

            response = self.client.chat.completions.create(

                model="llama-3.1-8b-instant",

                messages=[
                    {
                        "role": "system",
                        "content":
                        "You are an expert QA automation engineer."
                    },

                    {
                        "role": "user",
                        "content": f"""
                        Generate QA test cases for:

                        {requirement}

                        Include:
                        Positive tests
                        Negative tests
                        Edge cases
                        Security tests
                        """
                    }
                ]
            )


            result = (
                response
                .choices[0]
                .message
                .content
            )


            tests = [
                item.strip()

                for item in result.split("\n")

                if item.strip()
            ]


            return {

                "model": "Llama",

                "status": "success",

                "tests": tests
            }


        except Exception as error:


            return {

                "model": "Llama",

                "status": "failed",

                "error": repr(error),

                "tests": [
                    "Llama fallback activated"
                ]
            }