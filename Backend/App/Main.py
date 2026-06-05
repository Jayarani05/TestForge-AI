from fastapi import FastAPI

app = FastAPI(
    title="TestForge AI",
    description="AI Agentic QA Automation Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "TestForge AI Backend Running"
    }