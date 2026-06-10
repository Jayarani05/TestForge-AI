from fastapi import (
    FastAPI,
    Request
)

from fastapi.middleware.cors import (
    CORSMiddleware
)

from fastapi.responses import (
    JSONResponse
)


# ===========================
# API ROUTERS
# ===========================

from app.api.health import (
    router as health_router
)

from app.api import generation

from app.api.export import (
    router as export_router
)

from app.api.execution import (
    router as execution_router
)

from app.api.healing import (
    router as healing_router
)

from app.api.cicd import (
    router as cicd_router
)

from app.api.repository import (
    router as repository_router
)

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

from app.api import bug

from app.api.workflow import (
    router as workflow_router
)

# ===========================
# DATABASE
# ===========================

from app.database.connection import (
    engine,
    Base
)

from app.database import models

from app.api.code_generator import (
    router as code_router
)

from dotenv import load_dotenv

load_dotenv()

# ===========================
# APP CONFIG
# ===========================

app = FastAPI(

    title="TestForge AI",

    description=(
        "AI Agentic QA Automation Platform"
    ),

    version="1.0.0"

)



# ===========================
# CORS CONFIG
# ===========================

app.add_middleware(

    CORSMiddleware,


    allow_origins=[

        "http://localhost:5173",

        "http://127.0.0.1:5173",

        "http://localhost:3000"

    ],


    allow_credentials=True,


    allow_methods=[

        "*"

    ],


    allow_headers=[

        "*"

    ]

)



# ===========================
# ROUTERS
# ===========================


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

    workflow_router,

    prefix="/api/v1"

)

app.include_router(

    code_router,

    prefix="/api/v1"

)


# ===========================
# DATABASE TABLE CREATION
# ===========================

Base.metadata.create_all(
    bind=engine
)



# ===========================
# ROOT API
# ===========================

@app.get("/")
def root():

    return {

        "status":
        "success",


        "message":
        "TestForge AI Backend Running"

    }



# ===========================
# GLOBAL ERROR HANDLER
# ===========================

@app.exception_handler(
    Exception
)
async def global_exception_handler(

    request: Request,

    exc: Exception

):

    print(
        "\n========== TESTFORGE ERROR =========="
    )

    print(
        str(exc)
    )

    print(
        "=====================================\n"
    )


    return JSONResponse(


        status_code=500,


        headers={

            "Access-Control-Allow-Origin":
            "http://localhost:5173",


            "Access-Control-Allow-Credentials":
            "true"

        },


        content={


            "status":
            "error",


            "message":
            str(exc)


        }


    )



# ===========================
# PRINT ROUTES
# ===========================

print(
    "\n========== TESTFORGE ROUTES =========="
)


for route in app.routes:

    print(
        route.path
    )


print(
    "======================================\n"
)