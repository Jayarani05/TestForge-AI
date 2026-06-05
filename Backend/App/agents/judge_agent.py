class JudgeAgent:


    def evaluate(
        self,
        llm_responses
    ):

        scores = []


        for response in llm_responses:

            score = self.calculate_score(
                response
            )


            scores.append(
                {
                    "model": response["model"],
                    "score": score,
                    "tests": response["tests"]
                }
            )


        best_response = max(
            scores,
            key=lambda x: x["score"]
        )


        return {

            "evaluation": scores,

            "selected_model":
                best_response["model"],

            "optimized_tests":
                best_response["tests"]
        }



    def calculate_score(
        self,
        response
    ):

        score = 0


        score += len(
            response["tests"]
        ) * 10


        keywords = [
            "security",
            "edge",
            "negative",
            "validation"
        ]


        for test in response["tests"]:

            for keyword in keywords:

                if keyword.lower() in test.lower():

                    score += 5


        return score