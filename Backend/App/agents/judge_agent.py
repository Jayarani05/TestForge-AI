class JudgeAgent:


    def evaluate(
        self,
        llm_outputs
    ):

        evaluations = []


        for output in llm_outputs:


            result = (
                self.calculate_score(
                    output
                )
            )


            evaluations.append(

                {

                    "model":
                    output["model"],


                    "score":
                    result["score"],


                    "strengths":
                    result["strengths"],


                    "tests":
                    output["tests"]

                }

            )


        winner = max(

            evaluations,

            key=lambda item:
            item["score"]

        )


        return {

            "evaluation":
            evaluations,


            "selected_model":
            winner["model"],


            "confidence_score":
            winner["score"],


            "selection_reason":
            self.generate_reason(
                winner
            ),


            "optimized_tests":
            winner["tests"]

        }




    def calculate_score(
        self,
        response
    ):


        tests = (

            " ".join(
                response["tests"]
            )

            .lower()

        )


        score = 0


        strengths = []



        # 1. Test coverage - 30

        test_count = len(
            response["tests"]
        )


        if test_count >= 30:

            score += 30

            strengths.append(
                "Excellent coverage"
            )


        elif test_count >= 15:

            score += 20

            strengths.append(
                "Good coverage"
            )


        else:

            score += 10



        # 2. Security depth - 25

        security_keywords = [

            "security",
            "authentication",
            "authorization",
            "sql",
            "xss",
            "csrf",
            "token",
            "encryption",
            "vulnerability",
            "attack"

        ]


        security_score = sum(

            1

            for word in security_keywords

            if word in tests

        )


        score += min(

            security_score * 5,

            25

        )


        if security_score:

            strengths.append(
                "Strong security testing"
            )



        # 3. Edge cases - 20


        edge_keywords = [

            "edge",
            "boundary",
            "limit",
            "large",
            "special",
            "concurrent",
            "timeout"

        ]


        edge_score = sum(

            1

            for word in edge_keywords

            if word in tests

        )


        score += min(

            edge_score * 4,

            20

        )


        if edge_score:

            strengths.append(
                "Covers edge scenarios"
            )



        # 4. Structure quality - 15


        structure_keywords = [

            "steps",
            "expected",
            "precondition",
            "scenario",
            "verify"

        ]


        structure_score = sum(

            1

            for word in structure_keywords

            if word in tests

        )


        score += min(

            structure_score * 3,

            15

        )


        if structure_score:

            strengths.append(
                "Well structured test cases"
            )



        # 5. Duplicate penalty


        unique_tests = len(

            set(
                response["tests"]
            )

        )


        duplicate_count = (

            len(response["tests"])
            -
            unique_tests

        )


        score -= (

            duplicate_count * 2

        )



        return {

            "score":
            max(
                score,
                0
            ),


            "strengths":
            strengths

        }



    def generate_reason(
        self,
        winner
    ):


        return (

            f"{winner['model']} selected because of "

            +

            ", ".join(
                winner["strengths"]
            )

        )