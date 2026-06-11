import re

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

You are TestForge AI Automation Code Agent.

You are a senior SDET engineer.

Your job:
Convert MANUAL QA TEST CASES into REAL executable automation scripts.



===========================
PROJECT CONTEXT
===========================

{repo_context}



===========================
TEST CASES
===========================

{test_cases}



===========================
TARGET
===========================

Language:
{language}


Framework:
{framework}





Generate complete automation code.



STRICT RULES:


1. Do NOT copy test cases as comments.

2. Create separate test function for each test case.

3. Function names should match test scenarios.

4. Implement:

- imports
- driver setup
- browser launch
- test actions
- validations
- assertions
- teardown


5. Positive tests:
Validate successful workflows.


6. Negative tests:
Validate error handling.


7. Edge cases:
Validate boundary scenarios.


8. NEVER write:

assert True


9. Every test must contain meaningful assertions.


10. Use:

pytest

selenium webdriver


11. Use class:

TestGeneratedFlow


12. Include:

setup_method()

teardown_method()



Example format:


import pytest

from selenium import webdriver


class TestGeneratedFlow:


    def setup_method(self):

        self.driver = webdriver.Chrome()



    def teardown_method(self):

        self.driver.quit()




    def test_login_success(self):

        driver = self.driver

        driver.get("APP_URL")

        # actions here

        assert condition




Return ONLY python code.

No markdown.

No explanation.


"""





        response = self.llm.generate_response(

            prompt

        )






        clean = self.clean_code(

            response

        )





        return {

            "status":"success",

            "framework":framework,

            "language":language,

            "code":clean

        }









    def clean_code(

        self,

        code

    ):




        code = code.replace(

            "```python",

            ""

        )



        code = code.replace(

            "```",

            ""

        )




        return code.strip()