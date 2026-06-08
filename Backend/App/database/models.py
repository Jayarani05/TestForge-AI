from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    JSON,
    DateTime
)

from sqlalchemy.sql import func

from app.database.connection import Base




class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String
    )

    email = Column(
        String,
        unique=True,
        index=True
    )

    hashed_password = Column(
        String
    )






class Project(Base):

    __tablename__ = "projects"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String
    )

    description = Column(
        String
    )

    technology = Column(
        String
    )

    owner_id = Column(
        Integer,
        ForeignKey(
            "users.id"
        )
    )








class GenerationHistory(Base):

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
        String
    )


    result = Column(
        JSON
    )


    created_at = Column(
        DateTime,
        server_default=func.now()
    )








class ExecutionHistory(Base):

    __tablename__ = "execution_history"

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


    result = Column(
        JSON
    )


    created_at = Column(
        DateTime,
        server_default=func.now()
    )


class BugReport(Base):

    __tablename__ = "bug_reports"

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

    error = Column(
        String
    )

    result = Column(
        JSON
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )


class RepositoryAnalysis(Base):

    __tablename__ = "repository_analysis"

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

    repo_url = Column(
        String
    )

    result = Column(
        JSON
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )


class CICDHistory(Base):

    __tablename__ = "cicd_history"


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


    tool = Column(
        String
    )


    result = Column(
        JSON
    )


    created_at = Column(
        DateTime,
        server_default=func.now()
    )