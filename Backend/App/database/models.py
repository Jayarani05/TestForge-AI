from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime
)


from datetime import datetime


from app.database.connection import Base



class GenerationHistory(
    Base
):

    __tablename__ = "generation_history"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    user_story = Column(
        Text
    )


    generated_output = Column(
        Text
    )


    created_at = Column(

        DateTime,

        default=datetime.utcnow

    )