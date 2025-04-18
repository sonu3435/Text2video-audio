from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from moviepy.editor import ImageSequenceClip, AudioFileClip
import shutil
import os

app = FastAPI()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post("/generate-video")
async def generate_video(images: list[UploadFile] = File(...), audio: UploadFile = File(...)):
    image_paths = []
    for idx, img in enumerate(images):
        path = os.path.join(UPLOAD_DIR, f"img_{idx}.png")
        with open(path, "wb") as buffer:
            shutil.copyfileobj(img.file, buffer)
        image_paths.append(path)

    audio_path = os.path.join(UPLOAD_DIR, "voice.mp3")
    with open(audio_path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    # Create video clip
    clip = ImageSequenceClip(image_paths, fps=1)  # 1 img/sec
    audioclip = AudioFileClip(audio_path)
    clip = clip.set_audio(audioclip)

    output_path = os.path.join(OUTPUT_DIR, "final_video.mp4")
    clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

    return FileResponse(output_path, media_type="video/mp4", filename="final_video.mp4")
