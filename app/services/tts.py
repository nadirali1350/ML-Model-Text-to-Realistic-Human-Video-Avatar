import os
from typing import Optional

from app.settings import settings


class TextToSpeechService:
    def __init__(self) -> None:
        os.makedirs(settings.audio_dir, exist_ok=True)

    async def synthesize(self, text: str, voice_clone_audio_url: Optional[str]) -> str:
        import soundfile as sf
        import numpy as np

        sample_rate = 22050
        duration_seconds = max(2, int(len(text.split()) / 2))
        samples = np.zeros(sample_rate * duration_seconds, dtype=np.float32)

        output_path = os.path.join(settings.audio_dir, "tts_placeholder.wav")
        sf.write(output_path, samples, sample_rate)
        return output_path
