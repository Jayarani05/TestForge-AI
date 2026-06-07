# from fastapi import (
#     APIRouter,
#     Depends
# )


# from sqlalchemy.orm import Session


# from app.database.session import (
#     get_db
# )


# from app.security.auth import (
#     get_current_user
# )


# from app.database.models import (
#     Project,
#     GenerationHistory
# )



# router = APIRouter(

#     prefix="/dashboard",

#     tags=["Dashboard"]

# )



# @router.get(
#     "/"
# )

# def get_dashboard(

#     db: Session = Depends(
#         get_db
#     ),


#     current_user = Depends(
#         get_current_user
#     )

# ):


#     total_projects = (

#         db.query(Project)

#         .filter(

#             Project.owner_id
#             ==
#             current_user.id

#         )

#         .count()

#     )



#     total_generations = (

#         db.query(GenerationHistory)

#         .filter(

#             GenerationHistory.user_id
#             ==
#             current_user.id

#         )

#         .count()

#     )



#     return {


#         "user": {


#             "name":
#             current_user.name,


#             "email":
#             current_user.email,


#             "role":
#             current_user.role

#         },


#         "analytics": {


#             "total_projects":
#             total_projects,


#             "total_generations":
#             total_generations,


#             "total_executions":
#             0,


#             "bugs_found":
#             0

#         }

#     }

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









    return {


        "projects":

        total_projects,



        "generated_tests":

        total_generations,



        "executions":

        0,



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