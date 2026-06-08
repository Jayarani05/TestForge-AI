from app.exporters.excel_exporter import ExcelExporter


data = {

"positive_tests":[

{
"id":"TC001",
"title":"Verify login",
"type":"POS",
"priority":"High"
}

]

}


exporter = ExcelExporter()


print(
    exporter.export(data)
)