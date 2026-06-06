from openpyxl import Workbook


class ExcelExporter:


    def export(
        self,
        test_cases
    ):


        workbook = Workbook()

        sheet = workbook.active

        sheet.title = "Test Cases"


        sheet.append(
            [
                "ID",
                "Title",
                "Type",
                "Priority"
            ]
        )


        for category, tests in test_cases.items():


            for test in tests:


                sheet.append(

                    [

                        test.get(
                            "id"
                        ),


                        test.get(
                            "title"
                        ),


                        test.get(
                            "type"
                        ),


                        test.get(
                            "priority"
                        )

                    ]

                )


        path = (
            "exports/test_cases.xlsx"
        )


        workbook.save(
            path
        )


        return path