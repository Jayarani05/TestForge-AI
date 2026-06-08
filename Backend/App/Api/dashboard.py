
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

    Project,

    GenerationHistory

)

from app.database.models import ExecutionHistory

from app.database.models import BugReport



router = APIRouter(

    prefix="/dashboard",

    tags=[

        "Dashboard"

    ]

)







@router.get(

    "/"

)


def dashboard(


    db:Session = Depends(

        get_db

    ),



    current_user = Depends(

        get_current_user

    )


):




    total_projects = (


        db.query(Project)

        .filter(

            Project.owner_id == current_user.id

        )

        .count()


    )







    total_generations = (


        db.query(

            GenerationHistory

        )


        .filter(

            GenerationHistory.user_id

            ==

            current_user.id

        )


        .count()


    )







    recent = (


        db.query(

            GenerationHistory

        )


        .filter(

            GenerationHistory.user_id

            ==

            current_user.id

        )


        .order_by(

            GenerationHistory.id.desc()

        )


        .limit(5)


        .all()


    )

    executions = (
    db.query(ExecutionHistory)
    .filter(
        ExecutionHistory.user_id
        ==
        current_user.id
    )
    .count()
    )


    bugs = (
    db.query(BugReport)
    .filter(
        BugReport.user_id
        ==
        current_user.id
    )
    .count()
    )

    return {


        "projects":

        total_projects,



        "generated_tests":

        total_generations,



        "executions": executions,



        "bugs":

        0,



        "recent_activity":

        [

            {

                "id":

                item.id,



                "story":

                item.user_story


            }

            for item in recent

        ]


    }