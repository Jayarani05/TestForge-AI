from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session


from app.agents.bug_analyzer_agent import (
    BugAnalyzerAgent
)


from app.database.session import (
    get_db
)


from app.database.models import (
    BugReport
)


from app.security.auth import (
    get_current_user
)




router = APIRouter(

    prefix="/bugs",

    tags=["Bug Analyzer"]

)



agent = BugAnalyzerAgent()






@router.post("/analyze")

def analyze_bug(

    request:dict,

    db:Session = Depends(get_db),

    current_user = Depends(get_current_user)

):



    execution_result = request.get(
        "execution_result",
        request
    )



    result = agent.analyze(

        execution_result

    )





    bug = BugReport(

        user_id=current_user.id,


        project_id=request.get(
            "project_id"
        ),


        error=str(
            execution_result
        ),


        result=result

    )



    db.add(
        bug
    )


    db.commit()





    return {

        "status":

        "success",


        "analysis":

        result

    }