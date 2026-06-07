import json
import google.generativeai as genai

from app.core.config import settings


genai.configure(
    api_key=settings.GEMINI_API_KEY
)



def analyze_requirement(user_story: str):

    model = genai.GenerativeModel(
        "gemini-1.5-flash"
    )


    prompt = f"""

You are a senior QA requirement analyst.

Analyze this user story:

{user_story}


Return only JSON:

{{
"functional_requirements":[],

"non_functional_requirements":[],

"sentiment":{{

"type":"",
"confidence":0,
"reason":""

}},

"risk_analysis":{{

"risk_level":"",
"risks":[]

}}

}}

"""


    response = model.generate_content(
        prompt
    )


    clean = (
        response.text
        .replace("```json","")
        .replace("```","")
        .strip()
    )


    return json.loads(clean)