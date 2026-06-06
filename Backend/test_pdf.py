from app.exporters.pdf_exporter import PDFExporter


data = {

    "requirement_analysis": {

        "requirement":
        "User login"

    },


    "judge_result": {

        "selected_model":
        "DeepSeek",

        "confidence":
        95

    },


    "generated_test_cases": {

        "positive_tests":[

            {

            "id":"TC_POS_001",

            "title":"Verify login"

            }

        ]

    }

}


exporter = PDFExporter()


print(
    exporter.export(
        data
    )
)