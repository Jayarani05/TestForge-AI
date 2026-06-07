from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.database.models import (
    ExecutionHistory
)

from app.security.auth import (
    get_current_user
)


router = APIRouter(
    prefix="/execution",
    tags=["Execution"]
)



@router.post("/run")
def run_execution(
    data:dict,
    db:Session=Depends(get_db),
    current_user=Depends(get_current_user)
):


    result = {

        "status":"passed",

        "message":"Execution completed"

    }


    execution = ExecutionHistory(

        user_id=current_user.id,

        project_id=data.get(
            "project_id"
        ),

        result=result

    )


    db.add(execution)

    db.commit()



    return {

        "message":
        "Execution successful",

        "result":
        result

    }