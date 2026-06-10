from app.llm_services.gemini_service import (
    GeminiService
)





class CodeAgent:


    def __init__(self):

        self.llm = GeminiService()







    def generate_code(

        self,

        test_cases,

        repo_context,

        language="python",

        framework="pytest"

    ):



        prompt = f"""

You are TestForge AI Code Generation Agent.

Convert the generated QA test cases into
real executable automation test scripts.


========================
PROJECT CONTEXT
========================

{repo_context}


========================
TEST CASES
========================

{test_cases}


========================
OUTPUT CONFIG
========================

Language:
{language}


Framework:
{framework}



Generate:

- imports
- setup code
- test functions
- assertions
- teardown


Rules:

Return ONLY executable code.
No explanation.
No markdown.

"""





        result = (

            self.llm.generate_response(

                prompt

            )

        )



        return result