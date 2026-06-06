from fastapi import APIRouter

from pydantic import BaseModel

from typing import Dict, Any


from app.services.export_service import (
    ExportService
)


router = APIRouter(
    prefix="/export",
    tags=["Export"]
)



class ExportRequest(BaseModel):


    export_type: str


    data: Dict[str, Any]




@router.post("")
def export_file(
    request: ExportRequest
):


    service = ExportService()


    file_path = service.export(

        request.export_type,

        request.data

    )


    return {


        "status":
        "success",


        "message":
        "File exported successfully",


        "file_path":
        file_path

    }