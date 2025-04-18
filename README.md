# Text2video-audio
This project converts text into video and audio. It uses technologies like MoviePy, FastAPI, and gTTS (Google Text-to-Speech).

🎬 Text-to-Video & Audio Converter
This project enables users to convert plain text into a video with synchronized audio narration. It’s built using FastAPI for the backend, MoviePy for video creation, and gTTS (Google Text-to-Speech) for generating audio from text.


🚀 Features
✅ Convert plain text into narrated videos

🎙️ Generate audio from text using gTTS

🎞️ Create dynamic videos using MoviePy

⚡ Fast and scalable backend with FastAPI

🔄 Easy to integrate into other applications or frontend interfaces

🛠️ Tech Stack

Technology	Description
FastAPI	Web framework for building APIs
MoviePy	Python module for video editing
gTTS	Google Text-to-Speech library for audio synthesis
Python	Core language used in development
🧰 Installation
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/text-to-video-audio.git
cd text-to-video-audio
2. Create and activate a virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
🚦 Run the Server
bash
Copy
Edit
uvicorn main:app --reload
The API will be available at: http://127.0.0.1:8000

Swagger Docs: http://127.0.0.1:8000/docs

📂 Project Structure
graphql
Copy
Edit
.
├── main.py                 # FastAPI app entry point
├── video_generator.py      # Handles video and audio generation
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
📌 Usage
You can make a POST request with text data like this:

bash
Copy
Edit
curl -X POST "http://127.0.0.1:8000/generate" -H "Content-Type: application/json" -d '{"text": "Hello, world!"}'
The response will include a video file with audio narration.

✨ Future Improvements
Support for multiple languages

Custom voice options

Background music integration

Web frontend interface


