from typing import Optional, Dict

from app.services.tts import TextToSpeechService
from app.services.sadtalker import SadTalkerService
from app.services.wav2lip import Wav2LipRefiner


class SynthesisPipeline:
    def __init__(self) -> None:
        self.tts = TextToSpeechService()
        self.driver = SadTalkerService()
        self.refiner = Wav2LipRefiner()

    async def run(self, text: str, avatar_id: str, voice_clone_audio_url: Optional[str]) -> Dict[str, str]:
        audio_path = await self.tts.synthesize(text=text, voice_clone_audio_url=voice_clone_audio_url)
        video_path = await self.driver.generate_video(avatar_id=avatar_id, audio_path=audio_path)
        refined_video_path = await self.refiner.refine(video_path=video_path, audio_path=audio_path)
        return {"video_path": refined_video_path}
