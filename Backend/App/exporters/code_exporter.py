import os


class CodeExporter:


    def export(
        self,
        code,
        language
    ):


        os.makedirs(
            "exports",
            exist_ok=True
        )


        extension = (
            self.get_extension(
                language
            )
        )


        file_name = (
            f"generated_test{extension}"
        )


        path = os.path.join(
            "exports",
            file_name
        )


        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:


            file.write(
                code
            )


        return path




    def get_extension(
        self,
        language
    ):


        extensions = {


            "python":
            ".py",


            "java":
            ".java",


            "javascript":
            ".spec.js"


        }


        return extensions.get(

            language.lower(),

            ".txt"

        )