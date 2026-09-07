from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

from app.services.product import ProductService

router = APIRouter()


class ProductRequest(BaseModel):
    image_base64: Optional[str] = None
    barcode: Optional[str] = None


@router.post("/")
def analyze_product(req: ProductRequest):
    return ProductService.analyze_product_image(
        image_b64=req.image_base64,
        barcode=req.barcode
    )