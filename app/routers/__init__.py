"""
API Routers for PASLAR Daily Life Assistant endpoints.
"""

from .voice import router as voice_router
from .shopping import router as shopping_router
from .product import router as product_router
from .medication import router as medication_router

__all__ = [
    "voice_router",
    "shopping_router",
    "product_router",
    "medication_router",
]