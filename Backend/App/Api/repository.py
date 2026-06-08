from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.security.auth import (
    get_current_user
)

from app.database.models import (
    RepositoryAnalysis
)

from app.agents.repository_agent import (
    RepositoryAgent
)


router = APIRouter(
    prefix="/repository",
    tags=["Repository"]
)



@router.post("/analyze")
def analyze_repository(
    request:dict,
    db:Session=Depends(get_db),
    current_user=Depends(get_current_user)
):

    agent = RepositoryAgent()


    result = agent.analyze(
        request.get(
            "repo_url"
        )
    )


    repo = RepositoryAnalysis(

        user_id=current_user.id,

        repo_url=request.get(
            "repo_url"
        ),

        result=result
    )


    db.add(repo)

    db.commit()



    return {

        "status":"success",

        "analysis":result

    }





@router.get("/history")
def repo_history(
    db:Session=Depends(get_db),
    current_user=Depends(get_current_user)
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