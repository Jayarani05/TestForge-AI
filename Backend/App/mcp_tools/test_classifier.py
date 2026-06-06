class TestClassifier:


    def classify(
        self,
        tests
    ):


        result = {

            "positive_tests": [],

            "negative_tests": [],

            "edge_cases": [],

            "security_tests": []

        }


        counters = {

            "positive":1,
            "negative":1,
            "edge":1,
            "security":1

        }



        for test in tests:


            text = test.lower()


            if any(
                word in text

                for word in [

                    "sql",
                    "xss",
                    "csrf",
                    "attack",
                    "security",
                    "token",
                    "encryption",
                    "unauthorized"

                ]

            ):


                result["security_tests"].append(

                    self.create_case(

                        "TC_SEC",

                        counters["security"],

                        test,

                        "Critical"

                    )

                )


                counters["security"] += 1



            elif any(

                word in text

                for word in [

                    "invalid",
                    "fail",
                    "error",
                    "empty",
                    "wrong"

                ]

            ):


                result["negative_tests"].append(

                    self.create_case(

                        "TC_NEG",

                        counters["negative"],

                        test,

                        "High"

                    )

                )


                counters["negative"] += 1



            elif any(

                word in text

                for word in [

                    "edge",
                    "limit",
                    "boundary",
                    "large",
                    "special"

                ]

            ):


                result["edge_cases"].append(

                    self.create_case(

                        "TC_EDGE",

                        counters["edge"],

                        test,

                        "Medium"

                    )

                )


                counters["edge"] += 1



            else:


                result["positive_tests"].append(

                    self.create_case(

                        "TC_POS",

                        counters["positive"],

                        test,

                        "Medium"

                    )

                )


                counters["positive"] += 1



        return result



    def create_case(
        self,
        prefix,
        number,
        title,
        priority
    ):


        return {

            "id":
            f"{prefix}_{number:03}",


            "title":
            title,


            "priority":
            priority,


            "type":
            prefix.replace(
                "TC_",
                ""
            )

        }