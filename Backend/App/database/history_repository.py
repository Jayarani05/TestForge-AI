import json


from app.database.models import (
    GenerationHistory
)


def save_generation(
    db,
    story,
    result
):


    record = GenerationHistory(

        user_story=story,


        generated_output=json.dumps(
            result
        )

    )


    db.add(
        record
    )


    db.commit()


    db.refresh(
        record
    )


    return record