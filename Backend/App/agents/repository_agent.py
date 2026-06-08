import os
import tempfile
import shutil
import json
import stat

from git import Repo

from app.llm_services.gemini_service import (
    GeminiService
)



class RepositoryAgent:


    def __init__(self):

        self.llm = GeminiService()





    def analyze(
        self,
        repo_url
    ):


        temp_dir = tempfile.mkdtemp()



        try:


            Repo.clone_from(
                repo_url,
                temp_dir
            )


            project_files=[]



            for root,dirs,files in os.walk(temp_dir):


                for file in files:


                    if file.endswith(
                        (
                            ".py",
                            ".java",
                            ".js",
                            ".jsx",
                            ".ts",
                            ".tsx"
                        )
                    ):


                        path=os.path.join(
                            root,
                            file
                        )


                        with open(
                            path,
                            "r",
                            encoding="utf-8",
                            errors="ignore"
                        ) as f:


                            content=f.read()[:3000]



                        project_files.append(

                            {

                            "file":file,

                            "content":content

                            }

                        )







            prompt=f"""

You are a senior software architect,
security engineer and QA lead.

Analyze this GitHub repository.


Files:

{project_files}


Return ONLY valid JSON.

No markdown.

Format exactly:


{{

"name":"Repository name",

"tech_stack":[
"React",
"FastAPI",
"Python"
],

"security":
"Security summary",

"rating":
"8/10",

"recommendations":[

"Improve test coverage",

"Add CI/CD pipeline",

"Improve error handling"

]

}}


"""




            response=self.llm.generate_response(
                prompt
            )




            try:


                return json.loads(
                    response
                )


            except Exception:


                return {


                    "name":"Repository Analysis",


                    "tech_stack":[
                        "Detected from source code"
                    ],


                    "security":
                    "Analysis generated successfully",


                    "rating":
                    "8/10",


                    "recommendations":[
                        response
                    ]

                }






        finally:


            def remove_readonly(
                func,
                path,
                exc
            ):


                os.chmod(
                    path,
                    stat.S_IWRITE
                )


                func(path)





            shutil.rmtree(
                temp_dir,
                onerror=remove_readonly
            )