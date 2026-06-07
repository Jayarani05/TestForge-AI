from fastapi import (
    APIRouter,
    Depends
)


from sqlalchemy.orm import Session


from app.database.session import (
    get_db
)


from app.database.models import (
    Project
)


from app.schemas.project_schema import (
    ProjectCreate
)


from app.security.auth import (
    get_current_user
)

from app.database.models import (

    GenerationHistory

)

router = APIRouter(

    prefix="/projects",

    tags=["Projects"]

)



@router.post(
    "/create"
)

def create_project(

    request: ProjectCreate,


    db: Session = Depends(
        get_db
    ),


    current_user = Depends(
        get_current_user
    )

):


    project = Project(

        name=request.name,


        description=request.description,


        technology=request.technology,


        owner_id=current_user.id

    )


    db.add(project)


    db.commit()


    db.refresh(project)



    return {

        "message":
        "Project created successfully",


        "project_id":
        project.id

    }





@router.get(
    "/"
)

def get_projects(


    db: Session = Depends(
        get_db
    ),


    current_user = Depends(
        get_current_user
    )

):


    return (

        db.query(Project)


        .filter(

            Project.owner_id
            ==
            current_user.id

        )


        .all()

    )


@router.get(

    "/{project_id}/history"

)


def project_history(


    project_id:int,


    db:Session = Depends(
        get_db
    ),


    current_user = Depends(
        get_current_user
    )

):


    return (

        db.query(
            GenerationHistory
        )


        .filter(

            GenerationHistory.project_id
            ==
            project_id,


            GenerationHistory.user_id
            ==
            current_user.id

        )


        .all()

    )