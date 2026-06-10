from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session


from app.database.session import (
    get_db
)


from app.security.auth import (
    get_current_user
)


from app.database.models import (
    RepositoryAnalysis
)


from app.agents.repository_agent import (
    RepositoryAgent
)




# IMPORTANT - main.py imports this
router = APIRouter(

    prefix="/repository",

    tags=[
        "Repository"
    ]

)





@router.post(
    "/analyze"
)
def analyze_repository(

    request: dict,

    db: Session = Depends(
        get_db
    ),

    current_user = Depends(
        get_current_user
    )

):


    repo_url = request.get(
        "repo_url"
    )



    agent = RepositoryAgent()



    result = agent.analyze(

        repo_url

    )




    # save history

    repo = RepositoryAnalysis(

        user_id =
        current_user.id,


        repo_url =
        repo_url,


        result =
        result

    )



    db.add(
        repo
    )


    db.commit()





    return {


        "status":
        "success",


        "repo_url":
        repo_url,


        # contains:
        # name
        # tech_stack
        # repo_context

        "analysis":
        result

    }









@router.get(
    "/history"
)
def repository_history(


    db:Session = Depends(
        get_db
    ),


    current_user = Depends(
        get_current_user
    )


):



    return (

        db.query(
            RepositoryAnalysis
        )

        .filter(

            RepositoryAnalysis.user_id
            ==
            current_user.id

        )

        .all()

    )