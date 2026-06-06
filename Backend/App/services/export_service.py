from app.exporters.excel_exporter import (
    ExcelExporter
)

from app.exporters.pdf_exporter import (
    PDFExporter
)

from app.exporters.code_exporter import (
    CodeExporter
)



class ExportService:


    def __init__(self):


        self.excel_exporter = (
            ExcelExporter()
        )


        self.pdf_exporter = (
            PDFExporter()
        )


        self.code_exporter = (
            CodeExporter()
        )




    def export(
        self,
        export_type,
        data
    ):


        if export_type == "excel":


            return (

                self.excel_exporter
                .export(

                    data[
                        "generated_test_cases"
                    ]

                )

            )




        if export_type == "pdf":


            return (

                self.pdf_exporter
                .export(
                    data
                )

            )




        if export_type == "code":


            return (

                self.code_exporter
                .export(

                    data[
                        "code"
                    ],


                    data[
                        "language"
                    ]

                )

            )




        return None