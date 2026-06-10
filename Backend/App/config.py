import os

from dotenv import load_dotenv


load_dotenv()



class Settings:


    def __init__(self):


        self.GEMINI_API_KEY = os.getenv(
            "GEMINI_API_KEY"
        )


        self.GROQ_API_KEY = os.getenv(
            "GROQ_API_KEY"
        )


        self.DEEPSEEK_API_KEY = os.getenv(
            "DEEPSEEK_API_KEY"
        )


        self.JWT_SECRET_KEY = os.getenv(
            "JWT_SECRET_KEY",
            "testforge-ai-dev-secret-key-change-in-production"
        )
        
        # Validate JWT_SECRET_KEY is set and is a string
        if not self.JWT_SECRET_KEY or not isinstance(self.JWT_SECRET_KEY, str):
            raise ValueError(
                "JWT_SECRET_KEY must be set in .env file and must be a string. "
                "For production, use a strong random key."
            )



settings = Settings()