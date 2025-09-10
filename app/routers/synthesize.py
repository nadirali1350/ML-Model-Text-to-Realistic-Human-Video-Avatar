from fastapi import APIRouter, Form
from typing import Optional
from app.services.pipeline import SynthesisPipeline

router = APIRouter()

pipeline = SynthesisPipeline()


@router.post("")
async def synthesize(
    text: str = Form(...),
    avatar_id: str = Form(...),
    voice_clone_audio_url: Optional[str] = Form(None),
) -> dict:
    result = await pipeline.run(text=text, avatar_id=avatar_id, voice_clone_audio_url=voice_clone_audio_url)
    return result
