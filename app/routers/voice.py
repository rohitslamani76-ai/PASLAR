from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class VoiceRequest(BaseModel):
    audio_base64: str


class VoiceResponse(BaseModel):
    transcript: str
    response_text: str
    audio_base64: str


@router.post("/", response_model=VoiceResponse)
async def handle_voice(req: VoiceRequest):
    return VoiceResponse(
        transcript="Test voice input",
        response_text="Voice request received successfully.",
        audio_base64=req.audio_base64
    )