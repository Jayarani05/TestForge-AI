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

            "positive": 1,
            "negative": 1,
            "edge": 1,
            "security": 1

        }


        current_section = "positive"



        for test in tests:


            text = test.lower()



            # detect headings

            if "positive test" in text:

                current_section = "positive"
                continue


            if "negative test" in text:

                current_section = "negative"
                continue


            if "edge case" in text:

                current_section = "edge"
                continue


            if "security test" in text:

                current_section = "security"
                continue



            # ignore empty markdown separators

            if (
                text.strip() == ""
                or text.strip() == "---"
            ):

                continue



            if current_section == "positive":


                result["positive_tests"].append(

                    self.create_case(

                        "TC_POS",

                        counters["positive"],

                        test,

                        "Medium"

                    )

                )


                counters["positive"] += 1



            elif current_section == "negative":


                result["negative_tests"].append(

                    self.create_case(

                        "TC_NEG",

                        counters["negative"],

                        test,

                        "High"

                    )

                )


                counters["negative"] += 1




            elif current_section == "edge":


                result["edge_cases"].append(

                    self.create_case(

                        "TC_EDGE",

                        counters["edge"],

                        test,

                        "Medium"

                    )

                )


                counters["edge"] += 1




            elif current_section == "security":


                result["security_tests"].append(

                    self.create_case(

                        "TC_SEC",

                        counters["security"],

                        test,

                        "Critical"

                    )

                )


                counters["security"] += 1



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
            title.replace(
                "*",
                ""
            ).strip(),


            "priority":
            priority,


            "type":
            prefix.replace(
                "TC_",
                ""
            )

        }