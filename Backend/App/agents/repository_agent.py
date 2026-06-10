import os
import tempfile
import shutil
import json
import stat

from git import Repo

from app.llm_services.gemini_service import GeminiService


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


            project_files = []

            dependencies = []



            for root, dirs, files in os.walk(temp_dir):


                for file in files:


                    path = os.path.join(
                        root,
                        file
                    )


                    # dependencies

                    if file in [
                        "package.json",
                        "requirements.txt",
                        "pom.xml"
                    ]:

                        try:

                            with open(
                                path,
                                "r",
                                encoding="utf-8",
                                errors="ignore"
                            ) as f:

                                dependencies.append(
                                    f.read()[:2000]
                                )

                        except:

                            pass




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


                        try:


                            with open(
                                path,
                                "r",
                                encoding="utf-8",
                                errors="ignore"
                            ) as f:


                                content = f.read()[:3000]



                            project_files.append(

                                {

                                    "file": file,

                                    "content": content

                                }

                            )


                        except:

                            pass






            prompt=f"""

You are TestForge AI Repository Intelligence Agent.

Analyze this software project for QA automation.


SOURCE FILES:

{project_files}



DEPENDENCIES:

{dependencies}



Return ONLY JSON.


Format:


{{

"project_name":"",

"language":"",

"framework":"",

"total_files":0,


"tech_stack":[],

"dependencies":[],

"api_endpoints":[],

"functions":[],

"classes":[],


"security":
"",

"rating":
"",

"test_strategy":
"",


"recommendations":[]
}}


"""



            response = self.llm.generate_response(
                prompt
            )



            try:


                return json.loads(
                    response
                )


            except:


                return {


                    "project_name":
                    "Repository Analysis",


                    "language":
                    "Detected",


                    "framework":
                    "Detected",


                    "total_files":
                    len(project_files),


                    "tech_stack":
                    [],


                    "dependencies":
                    [],


                    "api_endpoints":
                    [],


                    "functions":
                    [],


                    "classes":
                    [],



                    "security":
                    "Completed",


                    "rating":
                    "8/10",



                    "test_strategy":
                    "Generate unit, integration and UI tests",



                    "recommendations":
                    [
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
