class JudgeAgent:


    def evaluate(
        self,
        llm_responses
    ):

        evaluations = []


        for response in llm_responses:


            score_details = (
                self.calculate_score(
                    response
                )
            )


            evaluations.append(
                {
                    "model":
                    response["model"],

                    "score":
                    score_details["total"],

                    "reason":
                    score_details["reason"],

                    "tests":
                    response["tests"]
                }
            )


        best = max(
            evaluations,
            key=lambda x: x["score"]
        )


        return {

            "evaluation":
            evaluations,


            "selected_model":
            best["model"],


            "confidence":
            best["score"],


            "selection_reason":
            best["reason"],


            "optimized_tests":
            best["tests"]

        }



    def calculate_score(
        self,
        response
    ):


        tests = " ".join(
            response["tests"]
        ).lower()


        score = 0


        reasons = []



        # coverage
        count = len(
            response["tests"]
        )


        if count >= 10:

            score += 40

            reasons.append(
                "High test coverage"
            )


        else:

            score += count * 3



        security_words = [

            "security",
            "authentication",
            "authorization",
            "sql",
            "xss",
            "vulnerability",
            "attack"
        ]


        if any(
            word in tests
            for word in security_words
        ):

            score += 25

            reasons.append(
                "Strong security validation"
            )



        edge_words = [

            "edge",
            "boundary",
            "limit",
            "exception"
        ]


        if any(
            word in tests
            for word in edge_words
        ):

            score += 20

            reasons.append(
                "Includes edge case testing"
            )



        negative_words = [

            "negative",
            "invalid",
            "failure",
            "error"
        ]


        if any(
            word in tests
            for word in negative_words
        ):

            score += 15

            reasons.append(
                "Covers negative scenarios"
            )



        return {

            "total":
            score,


            "reason":
            ", ".join(reasons)

        }