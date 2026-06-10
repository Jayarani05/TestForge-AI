from fastapi import FastAPI

from app.api.health import router as health_router
from app.api import generation
from app.api.export import (
    router as export_router
)

from app.api.execution import router as execution_router

from app.api.healing import (
    router as healing_router
)

from app.api.cicd import (
    router as cicd_router
)

from app.api.repository import (
    router as repository_router
)

from app.database.connection import (
    engine,
    Base
)
from app.database import models

from app.api.history import (
    router as history_router
)

from app.api.auth import (
    router as auth_router
)

from app.api.projects import (
    router as project_router
)

from app.api.dashboard import (
    router as dashboard_router
)

from fastapi.middleware.cors import (
    CORSMiddleware
)

from fastapi import Request

from fastapi.responses import JSONResponse

from app.api import bug


from app.api.repository import router as repo_router

app = FastAPI(
    title="TestForge AI",
    description="AI Agentic QA Automation Platform",
    version="1.0.0"
)

app.add_middleware(

    CORSMiddleware,


    allow_origins=[

        "http://localhost:5173",

        "http://127.0.0.1:5173"

    ],


    allow_credentials=True,


    allow_methods=[

        "*"

    ],


    allow_headers=[

        "*"

    ]

)


app.include_router(
    health_router,
    prefix="/api/v1"
)


app.include_router(
    generation.router,
    prefix="/api/v1"
)

app.include_router(
    export_router,
    prefix="/api/v1"
)

app.include_router(
    execution_router,
    prefix="/api/v1"
)

app.include_router(
    healing_router,
    prefix="/api/v1"
)

app.include_router(
    cicd_router,
    prefix="/api/v1"
)

app.include_router(
    repository_router,
    prefix="/api/v1"
)

app.include_router(
    history_router,
    prefix="/api/v1"
)

app.include_router(

    auth_router,

    prefix="/api/v1"

)

app.include_router(

    project_router,

    prefix="/api/v1"

)

app.include_router(

    dashboard_router,

    prefix="/api/v1"

)

app.include_router(
    bug.router,
    prefix="/api/v1"
)

app.include_router(
    repo_router,
    prefix="/api/v1"
)

Base.metadata.create_all(
    bind=engine
)

@app.get("/")
def root():
    return {
        "message": "TestForge AI Backend Running"
    }


@app.exception_handler(
    Exception
)

async def global_exception_handler(

    request: Request,


    exc: Exception

):

    return JSONResponse(

        status_code=500,


        content={

            "status":
            "error",


            "message":
            str(exc)

        }

        

    )


print("\n========== ROUTES ==========")

for route in app.routes:
    print(route.path)

print("============================\n")