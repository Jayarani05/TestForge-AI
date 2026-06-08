from openai import OpenAI

from app.config import DEEPSEEK_API_KEY


client = OpenAI(

    api_key=DEEPSEEK_API_KEY,

    base_url="https://openrouter.ai/api/v1"
)


try:

    response = client.chat.completions.create(

        model="deepseek/deepseek-chat",

        messages=[

            {
                "role": "user",
                "content": "Say hello"
            }

        ]

    )


    print(
        response
        .choices[0]
        .message
        .content
    )


except Exception as e:

    print(e)