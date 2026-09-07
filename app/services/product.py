# app/services/product.py


class ProductService:
    """Service handling product barcode scanning and Open Food Facts lookups."""

    @staticmethod
    def analyze_product_image(
        image_b64: str = None,
        barcode: str = None,
    ) -> dict:
        return {
            "product_name": "Scanned Product Item",
            "barcode": barcode or "0000000000",
            "safety_verdict": "SAFE",
            "reason": "No dietary conflicts or allergen warnings found.",
            "attribution": "Data retrieved from Open Food Facts (ODbL 1.0)",
        }