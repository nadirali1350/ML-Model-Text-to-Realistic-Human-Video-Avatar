import os
from app.settings import settings


class SadTalkerService:
    def __init__(self) -> None:
        os.makedirs(settings.video_dir, exist_ok=True)

    async def generate_video(self, avatar_id: str, audio_path: str) -> str:
        import ffmpeg

        output_path = os.path.join(settings.video_dir, f"{avatar_id}_raw.mp4")
        probe = ffmpeg.probe(audio_path)
        duration = float(probe['format']['duration'])
        (
            ffmpeg
            .input('color=c=black:s=320x320:d=' + str(duration), f='lavfi')
            .output(output_path, vcodec='libx264', pix_fmt='yuv420p', r=25)
            .overwrite_output()
            .run(quiet=True)
        )
        return output_path
