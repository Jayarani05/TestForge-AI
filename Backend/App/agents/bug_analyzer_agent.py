import json

from app.llm_services.gemini_service import (
    GeminiService
)



class BugAnalyzerAgent:


    def __init__(self):

        self.llm = GeminiService()




    def analyze(
        self,
        execution_result
    ):


        if execution_result.get("passed"):


            return {

                "severity":"LOW",

                "root_cause":
                "No failure detected",

                "possible_fix":
                "No fix required",

                "qa_recommendation":
                "All tests passed"

            }




        prompt = f"""

You are a senior QA automation engineer.

Analyze the failed test execution.


Failure:

{execution_result}


Return ONLY valid JSON.

Format:

{{
"severity":"",
"root_cause":"",
"possible_fix":"",
"qa_recommendation":""
}}

"""



        response = self.llm.generate_response(
            prompt
        )



        try:


            return json.loads(
                response
            )


        except Exception:


            return {

                "severity":
                "HIGH",

                "root_cause":
                response,

                "possible_fix":
                "Review failing code and logs",

                "qa_recommendation":
                "Add regression test coverage"

            }