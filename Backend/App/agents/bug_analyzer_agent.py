from app.llm_services.gemini_service import GeminiService


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

You are a senior QA engineer.

Analyze this failed automation result.


Execution Output:

{execution_result}


Generate:

1. Bug title
2. Severity (Low/Medium/High/Critical)
3. Root cause
4. Developer fix suggestion
5. QA recommendation


Return JSON format only.

"""


        response = self.llm.generate(
            prompt
        )


        return {


            "bug_found":
            True,


            "analysis":
            response

        }