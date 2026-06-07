import os

from dotenv import load_dotenv


load_dotenv()


GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)


GROQ_API_KEY = os.getenv(
    "GROQ_API_KEY"
)


DEEPSEEK_API_KEY = os.getenv(
    "DEEPSEEK_API_KEY"
)

JWT_SECRET_KEY = os.getenv(

    "JWT_SECRET_KEY"
)


settings = Settings()

if not GEMINI_API_KEY:
    print("Warning: GEMINI_API_KEY not found")

if not GROQ_API_KEY:
    print("Warning: GROQ_API_KEY not found")

if not DEEPSEEK_API_KEY:
    print("Warning: DEEPSEEK_API_KEY not found")