import os
import tempfile
import shutil
import json

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


            project_files = []


            for root, dirs, files in os.walk(
                temp_dir
            ):

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


                        path = os.path.join(
                            root,
                            file
                        )


                        with open(
                            path,
                            "r",
                            encoding="utf-8",
                            errors="ignore"
                        ) as f:


                            content = (
                                f.read()[:3000]
                            )


                        project_files.append(

                            {
                                "file":
                                file,

                                "content":
                                content
                            }

                        )


            prompt = f"""

You are a senior software architect and QA engineer.

Analyze this repository.


Files:

{project_files}


Find:

1. Project type
2. Programming languages
3. Frameworks
4. API endpoints
5. UI pages
6. Components
7. Testable features


Return ONLY JSON:

{{
"project_type":"",
"languages":[],
"frameworks":[],
"api_endpoints":[],
"ui_pages":[],
"features":[]
}}

"""


            response = (
                self.llm.generate_response(
                    prompt
                )
            )


            try:

                return json.loads(
                    response
                )


            except:

                return {
                    "raw_analysis":
                    response
                }



        finally:


            shutil.rmtree(
                temp_dir
            )