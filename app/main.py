# app/main.py

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.utils.safety import SafetyError
from app.routers import voice, shopping, product, medication


app = FastAPI(
    title="PASLAR Daily Life Assistant",
    version="1.0.0"
)


# Allow communication between frontend and backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Handle Safety Violations nicely
@app.exception_handler(SafetyError)
async def safety_exception_handler(request: Request, exc: SafetyError):
    return JSONResponse(
        status_code=403,
        content={
            "error": "SAFETY_VIOLATION",
            "message": exc.message
        },
    )


# Connect all the routers
app.include_router(
    voice.router,
    prefix="/api/voice",
    tags=["Voice"]
)

app.include_router(
    shopping.router,
    prefix="/api/shopping",
    tags=["Shopping"]
)

app.include_router(
    product.router,
    prefix="/api/analyze-product",
    tags=["Product Analysis"]
)

app.include_router(
    medication.router,
    prefix="/api/medication",
    tags=["Medication Reminders"]
)


@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "PASLAR Assistant API is running"
    }