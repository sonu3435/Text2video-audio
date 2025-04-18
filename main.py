from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from gtts import gTTS
from moviepy.editor import AudioFileClip, ColorClip
from fastapi.middleware.cors import CORSMiddleware
import os
import subprocess

app = FastAPI()

app = FastAPI()

# ✅ CORS fix
origins = [
    "http://127.0.0.1:5500",
    "http://0.0.0.0:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/text-to-video/")
async def text_to_video(text: str = Form(...)):
    # Step 1: Text to speech
    audio_path = "tts_audio.mp3"
    tts = gTTS(text)
    tts.save(audio_path)

    # Step 2: Get audio duration
    audio_clip = AudioFileClip(audio_path)
    duration = audio_clip.duration
    audio_clip.close()

    # Step 3: Make silent black video
    video_path = "silent_video.mp4"
    video_clip = ColorClip(size=(720, 480), color=(0, 0, 0), duration=duration)
    video_clip.write_videofile(video_path, fps=24, codec="libx264", audio=False)
    video_clip.close()

    # Step 4: Merge video + audio using ffmpeg
    output_path = "final_video.mp4"
    command = [
        "ffmpeg",
        "-y",  # overwrite
        "-i", video_path,
        "-i", audio_path,
        "-c:v", "copy",
        "-c:a", "aac",
        "-strict", "experimental",
        output_path
    ]
    subprocess.run(command)

    return FileResponse(output_path, media_type="video/mp4", filename="text_video.mp4")
