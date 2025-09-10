import os
import uuid
from typing import List, Optional
from fastapi import UploadFile

from app.settings import settings
from app.utils.files import save_upload_file


class AvatarIngestionService:
    def __init__(self) -> None:
        os.makedirs(settings.avatars_dir, exist_ok=True)

    async def ingest_avatar(self, name: str, description: Optional[str], files: List[UploadFile]) -> str:
        avatar_id = str(uuid.uuid4())
        avatar_dir = os.path.join(settings.avatars_dir, avatar_id)
        os.makedirs(avatar_dir, exist_ok=True)

        for file in files:
            await save_upload_file(file, os.path.join(avatar_dir, file.filename))

        # Save minimal metadata
        meta_path = os.path.join(avatar_dir, "meta.txt")
        with open(meta_path, "w", encoding="utf-8") as f:
            f.write(f"name: {name}\n")
            if description:
                f.write(f"description: {description}\n")
        return avatar_id
