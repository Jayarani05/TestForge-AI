from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship

from datetime import datetime

from app.database.connection import Base



class User(
    Base
):

    __tablename__ = "users"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    name = Column(
        String(100)
    )


    email = Column(
        String(150),
        unique=True,
        index=True
    )


    password = Column(
        String(255)
    )


    role = Column(
        String(50),
        default="QA Engineer"
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    histories = relationship(
        "GenerationHistory",
        back_populates="owner"
    )

    projects = relationship(

    "Project",

    back_populates="owner"

)

class GenerationHistory(
    Base
):

    __tablename__ = "generation_history"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    user_id = Column(

        Integer,

        ForeignKey(
            "users.id"
        )

    )


    project_id = Column(

        Integer,

        ForeignKey(
            "projects.id"
        )

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


    owner = relationship(

        "User",

        back_populates="histories"

    )


    project = relationship(

        "Project",

        back_populates="generations"

    )



class Project(
    Base
):

    __tablename__ = "projects"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    name = Column(
        String(150)
    )


    description = Column(
        Text
    )


    technology = Column(
        String(100)
    )


    owner_id = Column(

        Integer,

        ForeignKey(
            "users.id"
        )

    )


    created_at = Column(

        DateTime,

        default=datetime.utcnow

    )


    owner = relationship(

        "User",

        back_populates="projects"

    )


    generations = relationship(

    "GenerationHistory",

    back_populates="project"

)