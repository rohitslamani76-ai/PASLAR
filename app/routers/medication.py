from fastapi import APIRouter
from pydantic import BaseModel
from app.utils.safety import enforce_no_medication_changes

router = APIRouter()


class MedicationSchedule(BaseModel):
    medication_name: str
    time: str
    action_type: str = "remind"


@router.post("/")
def schedule_reminder(req: MedicationSchedule):
    enforce_no_medication_changes(req.action_type)

    return {
        "status": "SCHEDULED",
        "message": f"Reminder set for {req.medication_name} at {req.time}.",
    }