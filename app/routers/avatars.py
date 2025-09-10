from fastapi import APIRouter, UploadFile, File, Form
from typing import List, Optional
from app.services.ingestion import AvatarIngestionService

router = APIRouter()

ingestion_service = AvatarIngestionService()


@router.post("")
async def create_avatar(
    name: str = Form(...),
    files: List[UploadFile] = File(..., description="One or more images or a single video"),
    description: Optional[str] = Form(None),
) -> dict:
    avatar_id = await ingestion_service.ingest_avatar(name=name, description=description, files=files)
    return {"avatar_id": avatar_id}
