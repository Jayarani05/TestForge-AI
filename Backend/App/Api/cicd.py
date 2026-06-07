from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session


from app.database.session import get_db

from app.security.auth import (
    get_current_user
)


from app.database.models import (
    CICDHistory
)


from app.agents.cicd_agent import (
    CICDAgent
)




router = APIRouter(
    prefix="/cicd",
    tags=["CI/CD"]
)




@router.post("/generate")
def generate_pipeline(
    request:dict,
    db:Session = Depends(get_db),
    current_user = Depends(get_current_user)
):


    agent = CICDAgent()


    result = agent.generate(
        request
    )



    history = CICDHistory(

        user_id=current_user.id,

        tool=request.get(
            "tool"
        ),

        result=result

    )


    db.add(history)


    db.commit()



    return {

        "status":"success",

        "pipeline":result

    }







@router.get("/history")
def cicd_history(
    db:Session = Depends(get_db),
    current_user = Depends(get_current_user)
):


    return (

        db.query(CICDHistory)

        .filter(
            CICDHistory.user_id
            ==
            current_user.id
        )

        .all()

    )