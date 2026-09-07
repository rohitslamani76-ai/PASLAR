# app/utils/safety.py


class SafetyError(RuntimeError):
    """Raised whenever a request violates a DPR 'DO NOT ...' rule."""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


def enforce_no_medication_changes(action: str) -> None:
    """
    The DPR explicitly forbids any dosage-change request.
    Raises SafetyError if a medication change is attempted.
    """
    forbidden_actions = {
        "increase dose",
        "decrease dose",
        "change dose",
        "adjust medication",
        "stop medication",
        "start medication",
    }

    if action.lower() in forbidden_actions or "dose" in action.lower():
        raise SafetyError(
            "❌ DENIED: The Daily Life Assistant is not permitted to make medical claims, "
            "diagnoses, or medication-dosage decisions. Please contact your caregiver or physician."
        )