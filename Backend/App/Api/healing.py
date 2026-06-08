from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.self_healing_agent import (
    SelfHealingAgent
)


router = APIRouter(
    prefix="/healing",
    tags=["Self Healing"]
)



class HealingRequest(
    BaseModel
):

    failed_code: str

    error_log: str

    dom_snapshot: str




@router.post(
    "/repair"
)
def repair_test(
    request: HealingRequest
):

    agent = (
        SelfHealingAgent()
    )


    result = agent.heal(
        request.failed_code,
        request.error_log,
        request.dom_snapshot
    )


    return {

        "status":
        "success",


        "healed_result":
        result

    }