from fastapi import (
    APIRouter,
    Depends
)


from app.security.auth import (
    get_current_user
)


from app.agents.code_agent import (
    CodeAgent
)





router = APIRouter(

    prefix="/code",

    tags=[
        "Code Generation"
    ]

)





@router.post(
    "/generate"
)
def generate_code(


    request:dict,


    current_user=Depends(
        get_current_user
    )

):



    agent = CodeAgent()



    code = agent.generate_code(


        request.get(
            "test_cases"
        ),


        request.get(
            "repo_context"
        ),


        request.get(
            "language",
            "python"
        ),


        request.get(
            "framework",
            "pytest"
        )

    )





    return {


        "status":

        "success",


        "generated_code":

        code


    }