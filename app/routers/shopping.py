from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ShoppingRequest(BaseModel):
    item_name: str
    quantity: int = 1


@router.post("/")
def handle_shopping(req: ShoppingRequest):
    requires_approval = (
        "peanut" in req.item_name.lower()
        or "allergy" in req.item_name.lower()
    )

    if requires_approval:
        return {
            "status": "CAREGIVER_APPROVAL_REQUIRED",
            "message": "Item flagged due to dietary restriction. Request sent to caregiver.",
            "approval_id": "REQ-2026-0830-01",
        }

    return {
        "status": "APPROVED",
        "message": f"Successfully ordered {req.quantity}x {req.item_name}.",
        "order_id": "ORD-2026-0830-01",
    }