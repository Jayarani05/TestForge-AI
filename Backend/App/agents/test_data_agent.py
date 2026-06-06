import json

from app.llm_services.gemini_service import (
    GeminiService
)


class TestDataAgent:


    def __init__(
        self
    ):

        self.llm = GeminiService()



    def generate(
        self,
        requirement,
        test_cases
    ):


        prompt = f"""

You are a QA test data engineer.

Generate realistic test data.


Requirement:

{requirement}


Test Cases:

{test_cases}


Return ONLY JSON.

No markdown.

Format:

{{
"valid_data":[],

"invalid_data":[],

"edge_cases":[],

"security_data":[]
}}

"""


        response = (
            self.llm.generate_response(
                prompt
            )
        )


        try:

            return json.loads(
                response
            )


        except Exception:

            return {

                "raw_data":
                response

            }