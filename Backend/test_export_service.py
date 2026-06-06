from app.services.export_service import (
    ExportService
)



service = ExportService()


data = {


"generated_test_cases":{


"positive_tests":[

{

"id":"TC001",

"title":"Verify Login",

"type":"POS",

"priority":"High"

}

]

}

}


print(

    service.export(

        "excel",

        data

    )

)