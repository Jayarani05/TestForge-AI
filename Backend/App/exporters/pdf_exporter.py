from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


class PDFExporter:


    def export(
        self,
        data
    ):


        path = "exports/qa_report.pdf"


        document = SimpleDocTemplate(
            path
        )


        styles = getSampleStyleSheet()


        content = []


        content.append(

            Paragraph(
                "TestForge AI QA Report",
                styles["Title"]
            )

        )


        content.append(
            Spacer(
                1,
                20
            )
        )



        # Requirement


        if "requirement_analysis" in data:


            content.append(

                Paragraph(

                    "Requirement Analysis",

                    styles["Heading2"]

                )

            )


            content.append(

                Paragraph(

                    str(
                        data[
                            "requirement_analysis"
                        ]
                    ),

                    styles["Normal"]

                )

            )



        # Judge Result


        if "judge_result" in data:


            content.append(

                Paragraph(

                    "AI Judge Result",

                    styles["Heading2"]

                )

            )


            content.append(

                Paragraph(

                    str(
                        data[
                            "judge_result"
                        ]
                    ),

                    styles["Normal"]

                )

            )



        # Generated Tests


        if "generated_test_cases" in data:


            content.append(

                Paragraph(

                    "Generated Test Cases",

                    styles["Heading2"]

                )

            )


            tests = (
                data[
                    "generated_test_cases"
                ]
            )


            for category, items in tests.items():


                content.append(

                    Paragraph(

                        category,

                        styles["Heading3"]

                    )

                )


                for test in items:


                    content.append(

                        Paragraph(

                            f'{test["id"]} - {test["title"]}',

                            styles["Normal"]

                        )

                    )



        document.build(
            content
        )


        return path