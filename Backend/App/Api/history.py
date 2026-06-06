from fastapi import APIRouter,Depends

from sqlalchemy.orm import Session


from app.database.session import (
    get_db
)

from app.database.models import (
    GenerationHistory
)



router = APIRouter(
    prefix="/history",
    tags=["History"]
)



@router.get(
    "/"
)

def get_history(
    db:Session = Depends(get_db)
):


    return (

        db.query(
            GenerationHistory
        )

        .all()

    )