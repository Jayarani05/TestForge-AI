import json

from app.database.models import (
    GenerationHistory
)



def save_generation(
    db,
    user_id,
    project_id,
    user_story,
    result
):

    record = GenerationHistory(

        user_id=user_id,

        project_id=project_id,

        user_story=user_story,

        result=json.dumps(result)

    )


    db.add(record)

    db.commit()

    db.refresh(record)


    return record