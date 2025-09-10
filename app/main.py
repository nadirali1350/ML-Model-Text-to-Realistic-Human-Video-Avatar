from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.avatars import router as avatars_router
from app.routers.synthesize import router as synthesize_router

app = FastAPI(title="AvatarSynth API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(avatars_router, prefix="/avatars", tags=["avatars"])
app.include_router(synthesize_router, prefix="/synthesize", tags=["synthesize"])


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}
