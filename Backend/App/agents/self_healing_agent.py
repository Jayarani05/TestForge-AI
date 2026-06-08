import json

from app.llm_services.gemini_service import (
    GeminiService
)


class SelfHealingAgent:


    def __init__(self):

        self.llm = GeminiService()



    def heal(
        self,
        failed_code,
        error_log,
        dom_snapshot
    ):


        prompt = f"""

You are an expert Selenium automation engineer.

A test failed because of a broken locator.

Analyze the failure and repair it.


FAILED CODE:

{failed_code}


ERROR:

{error_log}


CURRENT HTML DOM:

{dom_snapshot}



Return ONLY JSON.

No markdown.

Format:

{{
"broken_locator":"",
"reason":"",
"suggested_locator":"",
"fixed_code":""
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

                "raw_response":
                response

            }