from app.llm_services.gemini_service import GeminiService
import json


class BugAnalyzerAgent:


    def __init__(self):

        self.llm = GeminiService()



    def analyze(
        self,
        execution_result
    ):


        if execution_result.get("passed"):

            return {

                "bug_found": False,

                "message":
                "All tests passed"

            }


        prompt = f"""

You are an expert QA automation engineer.

Analyze this failed test execution.


Execution Result:

{execution_result}


Return ONLY this JSON.

Do not generate test cases.
Do not add explanations.


{{
"title":"",
"severity":"",
"root_cause":"",
"possible_fix":"",
"qa_recommendation":""
}}

"""

        response = (
            self.llm.generate_response(
                prompt
            )
        )

        try:

            parsed = json.loads(
            response
            )

        except Exception:

            parsed = {
            "raw_analysis":
            response
            }


        return {

            "bug_found":
            True,


            "analysis":
            parsed

        }