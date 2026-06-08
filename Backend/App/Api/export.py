import json
import tempfile


from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)


from fastapi.responses import FileResponse


from sqlalchemy.orm import Session


from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)


from reportlab.lib.styles import (
    getSampleStyleSheet
)



from app.database.session import (
    get_db
)


from app.security.auth import (
    get_current_user
)


from app.database.models import (
    GenerationHistory
)




router = APIRouter(

    prefix="/export",

    tags=["Export"]

)






@router.get(
    "/{history_id}"
)

def export_generation(

    history_id:int,

    db:Session = Depends(get_db),

    current_user = Depends(get_current_user)

):



    history = (

        db.query(
            GenerationHistory
        )


        .filter(

            GenerationHistory.id == history_id,


            GenerationHistory.user_id
            ==
            current_user.id

        )


        .first()

    )




    if not history:


        raise HTTPException(

            status_code=404,

            detail="History not found"

        )






    file_path = tempfile.mktemp(

        suffix=".pdf"

    )





    document = SimpleDocTemplate(

        file_path

    )



    styles = getSampleStyleSheet()



    pdf_content = []







    # TITLE

    pdf_content.append(


        Paragraph(

            "TestForge AI - QA Automation Report",

            styles["Title"]

        )


    )



    pdf_content.append(

        Spacer(1,20)

    )








    # REQUIREMENT


    pdf_content.append(


        Paragraph(

            "Requirement",

            styles["Heading2"]

        )


    )



    pdf_content.append(

        Paragraph(

            history.user_story,

            styles["BodyText"]

        )

    )






    pdf_content.append(

        Spacer(1,20)

    )








    # TEST RESULT


    pdf_content.append(

        Paragraph(

            "Generated Test Cases",

            styles["Heading2"]

        )

    )





    output = json.dumps(

        history.result,

        indent=4

    )





    output = output.replace(

        "\n",

        "<br/>"

    )





    pdf_content.append(

        Paragraph(

            output,

            styles["Code"]

        )

    )







    document.build(

        pdf_content

    )






    return FileResponse(


        file_path,


        media_type="application/pdf",


        filename="TestForge_AI_Report.pdf"

    )