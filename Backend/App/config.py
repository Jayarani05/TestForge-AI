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
            "JWT_SECRET_KEY"
        )



settings = Settings()