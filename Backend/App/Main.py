from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.generation import router as test_router
from app.api.export import (
    router as export_router
)

from app.api.execution import router as execution_router

from app.api.healing import (
    router as healing_router
)

app = FastAPI(
    title="TestForge AI",
    description="AI Agentic QA Automation Platform",
    version="1.0.0"
)


app.include_router(
    health_router,
    prefix="/api/v1"
)


app.include_router(
    test_router,
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


@app.get("/")
def root():
    return {
        "message": "TestForge AI Backend Running"
    }