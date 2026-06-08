import json
import os

import google.generativeai as genai

from dotenv import load_dotenv


load_dotenv()



genai.configure(

    api_key=os.getenv(
        "GEMINI_API_KEY"
    )

)





def analyze_requirement(user_story:str):


    model = genai.GenerativeModel(
        "gemini-3.5-flash"
    )



    prompt=f"""

You are a senior QA requirement analyst.

Analyze this user story:

{user_story}


Return ONLY JSON:


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



    response=model.generate_content(
        prompt
    )



    clean=response.text.replace(
        "```json",
        ""
    ).replace(
        "```",
        ""
    ).strip()



    try:


        return json.loads(
            clean
        )



    except Exception:


        return {


            "functional_requirements":[],

            "non_functional_requirements":[],

            "sentiment":{

                "type":"Neutral",

                "confidence":0,

                "reason":"parse failed"

            },

            "risk_analysis":{

                "risk_level":"Unknown",

                "risks":[]

            }


        }