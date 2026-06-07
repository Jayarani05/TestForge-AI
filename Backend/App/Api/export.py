from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.security.auth import (
    get_current_user
)

from app.database.models import (
    GenerationHistory
)


router = APIRouter(
    prefix="/export",
    tags=["Export"]
)



@router.get(
    "/{history_id}"
)

def export_generation(
    history_id:int,
    db:Session = Depends(get_db),
    current_user = Depends(get_current_user)
):


    history = (
        db.query(GenerationHistory)

        .filter(
            GenerationHistory.id == history_id,

            GenerationHistory.user_id
            ==
            current_user.id
        )

        .first()
    )



    if not history:

        raise HTTPException(
            status_code=404,
            detail="History not found"
        )



    return {

        "project_id":
        history.project_id,


        "requirement":
        history.user_story,


        "generated_tests":
        history.result,


        "export_type":
        "json"

    }