from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session


from app.agents.qa_agent import (
    QAAgent
)


from app.schemas.story_schema import (
    UserStoryRequest
)


from app.database.session import (
    get_db
)


from app.database.history_repository import (
    save_generation
)


from app.security.auth import (

    get_current_user

)


from app.database.models import (

    Project

)


from fastapi import HTTPException


router = APIRouter(
    prefix="/tests",
    tags=["Test Generation"]
)



@router.post(
    "/generate"
)

def generate_tests(

    request: UserStoryRequest,


    db:Session = Depends(
        get_db
    ),


    current_user = Depends(
        get_current_user
    )

):


    project = (

    db.query(Project)

    .filter(

        Project.id == request.project_id,


        Project.owner_id == current_user.id

    )

    .first()

    )


    if not project:


        raise HTTPException(

            status_code=404,


            detail="Project not found"

        )

    agent = QAAgent()


    result = agent.process_story(

        request.user_story,


        request.output_type,


        request.language,


        request.framework,


        request.project_context

    )


    # save generated result in database

    save_generation(

        db,


        current_user.id,


        request.project_id,


        request.user_story,


        result

    )



    return {


        "status":
        "success",


        "message":
        "QA Agent executed successfully",


        "story":
        request.user_story,


        "agent_result":
        result

    }