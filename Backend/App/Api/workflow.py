from fastapi import APIRouter
from pydantic import BaseModel

import tempfile
import os

from git import Repo


router = APIRouter(
    prefix="/workflow",
    tags=["Workflow"]
)


class WorkflowRequest(BaseModel):

    repo_url:str

    user_story:str



def read_repository(path):

    context = ""


    allowed = [
        ".py",
        ".js",
        ".jsx",
        ".java",
        ".html",
        ".css"
    ]


    for root,dirs,files in os.walk(path):


        if ".git" in root:
            continue


        for file in files:


            if file.endswith(tuple(allowed)):


                full = os.path.join(
                    root,
                    file
                )


                try:

                    with open(
                        full,
                        "r",
                        encoding="utf-8"
                    ) as f:


                        context += f"""

FILE:
{file}

CODE:
{f.read()[:3000]}

"""


                except:

                    pass


    return context





@router.post("/generate-tests")
def generate_tests(
    data:WorkflowRequest
):


    temp = tempfile.mkdtemp()


    # clone repo

    Repo.clone_from(

        data.repo_url,

        temp

    )


    repo_context = read_repository(
        temp
    )



    # temporary AI response
    # connect Gemini here

    test_cases = f"""


Generated Test Cases


USER STORY:

{data.user_story}



Repository Understanding:

Analyzed source files successfully.


TEST CASE 1:

Verify application loads correctly


Steps:

1. Start application
2. Open main page
3. Validate UI rendering


Expected:

Application should load without errors



TEST CASE 2:

Validate user workflow


Steps:

1. Perform user action
2. Submit data
3. Verify response


Expected:

Correct response should be generated



TEST CASE 3:

Error handling validation


Steps:

1. Provide invalid input
2. Trigger failure scenario


Expected:

System handles errors properly


"""


    return {


        "repo_analyzed":
        True,


        "test_cases":
        test_cases

    }