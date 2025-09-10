## AvatarSynth API

A FastAPI service to generate realistic talking-head avatar videos from text. Supports uploading an avatar (images or a video) and synthesizing speech-driven video with planned integration of SadTalker, Wav2Lip, and Coqui XTTS v2.

### Setup

```bash
bash run.sh
```

### Endpoints
- POST `/avatars` — form fields: `name`, optional `description`, files: one or more images or a single video
- POST `/synthesize` — form fields: `text`, `avatar_id`, optional `voice_clone_audio_url`

Responses return file paths for now.
