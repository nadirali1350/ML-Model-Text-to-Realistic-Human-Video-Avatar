import os
from dataclasses import dataclass


@dataclass
class Settings:
	base_dir: str = os.getenv("AVATAR_SYNTH_BASE", "/workspace/data")

	@property
	def avatars_dir(self) -> str:
		return os.path.join(self.base_dir, "avatars")

	@property
	def audio_dir(self) -> str:
		return os.path.join(self.base_dir, "audio")

	@property
	def video_dir(self) -> str:
		return os.path.join(self.base_dir, "video")


settings = Settings()
