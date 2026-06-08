import subprocess
import tempfile
import os
import time


class TestExecutionAgent:


    def execute(
        self,
        code
    ):

        start_time = time.time()


        with tempfile.NamedTemporaryFile(
            suffix=".py",
            delete=False,
            mode="w",
            encoding="utf-8"
        ) as file:


            file.write(code)


            test_file = file.name


        try:


            result = subprocess.run(

                [
                    "pytest",
                    test_file,
                    "-v"
                ],

                capture_output=True,
                text=True,
                timeout=60

            )


            execution_time = round(
                time.time() - start_time,
                2
            )


            return {

                "status":
                "completed",


                "passed":
                result.returncode == 0,


                "execution_time":
                f"{execution_time}s",


                "logs":
                result.stdout,


                "errors":
                result.stderr

            }


        except Exception as e:


            return {

                "status":
                "failed",

                "error":
                str(e)

            }


        finally:


            if os.path.exists(
                test_file
            ):

                os.remove(
                    test_file
                )