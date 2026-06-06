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



router = APIRouter(
    prefix="/tests",
    tags=["Test Generation"]
)



@router.post(
    "/generate"
)

def generate_tests(

    request: UserStoryRequest,


    db: Session = Depends(
        get_db
    )

):


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