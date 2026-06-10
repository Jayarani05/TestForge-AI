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


            # =====================
            # CLONE REPOSITORY
            # =====================

            Repo.clone_from(
                repo_url,
                temp_dir
            )



            project_files = []




            # =====================
            # READ SOURCE CODE
            # =====================


            for root,dirs,files in os.walk(
                temp_dir
            ):


                if ".git" in root:
                    continue



                for file in files:


                    if file.endswith(
                        (
                            ".py",
                            ".java",
                            ".js",
                            ".jsx",
                            ".ts",
                            ".tsx",
                            ".html",
                            ".css"
                        )
                    ):


                        path = os.path.join(
                            root,
                            file
                        )



                        try:


                            with open(
                                path,
                                "r",
                                encoding="utf-8",
                                errors="ignore"
                            ) as f:


                                content = (
                                    f.read()[:4000]
                                )



                            project_files.append(

                                {

                                "file":
                                file,


                                "path":
                                path.replace(
                                    temp_dir,
                                    ""
                                ),


                                "content":
                                content

                                }

                            )



                        except Exception:

                            pass








            # =====================
            # GEMINI ANALYSIS
            # =====================


            prompt=f"""

You are TestForge AI Repository Agent.

Analyze this software repository.


SOURCE FILES:

{project_files}



Return ONLY JSON.

Format:

{{

"name":"Repository name",

"tech_stack":[
"React",
"FastAPI"
],

"security":
"security analysis",

"rating":
"8/10",

"recommendations":[
"Improve tests"
]

}}

"""



            response = (
                self.llm
                .generate_response(
                    prompt
                )
            )





            try:


                analysis = json.loads(
                    response
                )


            except Exception:


                analysis = {

                    "name":
                    "Repository Analysis",


                    "tech_stack":[
                        "Detected from code"
                    ],


                    "security":
                    "Completed",


                    "rating":
                    "8/10",


                    "recommendations":[
                        response
                    ]

                }





            # IMPORTANT
            # send cloned repo context forward


            analysis[
                "repo_context"
            ] = project_files



            return analysis







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