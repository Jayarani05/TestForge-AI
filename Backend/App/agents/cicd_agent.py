import json

from app.llm_services.gemini_service import (
    GeminiService
)


class CICDAgent:


    def __init__(self):

        self.llm = GeminiService()



    def generate(
        self,
        framework,
        language,
        tool
    ):


        prompt = f"""

You are a DevOps automation engineer.

Generate CI/CD pipeline configuration.


Language:
{language}


Test Framework:
{framework}


CI/CD Tool:
{tool}



Rules:

- Return ONLY JSON
- No explanation
- No markdown


Format:

{{
"tool":"",
"file_name":"",
"pipeline_code":""
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

                "raw_pipeline":
                response

            }