class ProjectContextAgent:


    def process(
        self,
        context
    ):


        if not context:


            return {


                "available":
                False,


                "message":
                "No project context provided"

            }


        return {


            "available":
            True,


            "url":
            context.get(
                "url"
            ),


            "elements":
            context.get(
                "elements",
                {}
            )

        }