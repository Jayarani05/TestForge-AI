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





router = APIRouter(

    tags=[
        "Test Generation"
    ]

)





@router.post(
    "/tests/generate"
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



    # =============================
    # QA AGENT PIPELINE
    # =============================


    agent = QAAgent()



    result = agent.process_story(


        request.user_story,


        request.output_type,


        request.language,


        request.framework,


        request.project_context


    )





    # save only if project exists

    try:


        if request.project_id:


            save_generation(

                db,

                current_user.id,

                request.project_id,

                request.user_story,

                result

            )


    except Exception:


        pass








    return {


        "status":

        "success",


        "message":

        "Repository based QA generation completed",


        "story":

        request.user_story,


        "agent_result":

        result


    }