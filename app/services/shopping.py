# app/services/shopping.py

class ShoppingService:
    """Service orchestrating shopping orders and caregiver permission checks."""

    @staticmethod
    def process_order(item_name: str, quantity: int = 1) -> dict:
        requires_approval = (
            "peanut" in item_name.lower()
            or "allergy" in item_name.lower()
        )

        if requires_approval:
            return {
                "status": "CAREGIVER_APPROVAL_REQUIRED",
                "message": f"Order for {item_name} requires caregiver approval.",
                "approval_id": "REQ-2026-PENDING",
            }

        return {
            "status": "APPROVED",
            "message": f"Ordered {quantity}x {item_name}.",
            "order_id": "ORD-2026-CONFIRMED",
        }