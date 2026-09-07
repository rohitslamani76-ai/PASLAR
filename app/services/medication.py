# app/services/medication.py

from app.utils.safety import enforce_no_medication_changes


class MedicationService:
    """Service handling medication reminders and schedule tracking."""

    @staticmethod
    def schedule_reminder(
        medication_name: str,
        time: str,
        action_type: str = "remind",
    ):
        # Enforce strict safety boundary: deny dosage changes
        enforce_no_medication_changes(action_type)

        return {
            "status": "SCHEDULED",
            "medication": medication_name,
            "scheduled_time": time,
            "message": f"Reminder set for {medication_name} at {time}.",
        }