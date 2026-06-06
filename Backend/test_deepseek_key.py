from app.config import DEEPSEEK_API_KEY


if DEEPSEEK_API_KEY:

    print(
        DEEPSEEK_API_KEY[:10]
    )

else:

    print(
        "DeepSeek key not loaded"
    )