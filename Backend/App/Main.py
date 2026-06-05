from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(
    title="TestForge AI",
    description="AI Agentic QA Automation Platform",
    version="1.0.0"
)

app.include_router(
    health_router,
    prefix="/api/v1"
)

@app.get("/")
def root():
    return {
        "message": "TestForge AI Backend Running"
}