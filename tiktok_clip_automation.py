# tiktok_clip_automation/main.py

from faster_whisper import WhisperModel
import subprocess
import os

VIDEO_PATH = "TOAST.mp4"
 # Replace with your input video
MODEL_SIZE = "medium"  # Options: tiny, base, small, medium, large-v2
DEVICE = "cpu"  # Use "cpu" if you don't have a GPU

# Step 1: Transcribe video
model = WhisperModel(MODEL_SIZE, device=DEVICE, compute_type="float16")
segments, _ = model.transcribe(VIDEO_PATH, beam_size=5)

# Step 2: Find highlight-worthy clips
keywords = ["no way", "omg", "insane", "what just happened", "clip that", "holy", "crazy"]
highlight_segments = []

for segment in segments:
    text = segment.text.lower()
    if any(k in text for k in keywords):
        start = max(0, segment.start - 3)
        end = segment.end + 3
        highlight_segments.append((start, end))

# Step 3: Auto-clip with ffmpeg
os.makedirs("clips", exist_ok=True)
for i, (start, end) in enumerate(highlight_segments):
    output_file = f"clips/clip_{i+1}.mp4"
    cmd = [
        "ffmpeg",
        "-ss", str(start),
        "-to", str(end),
        "-i", VIDEO_PATH,
        "-vf", "crop=ih*9/16:ih",
        "-c:v", "libx264",
        "-crf", "23",
        "-preset", "fast",
        output_file
    ]
    subprocess.run(cmd)

print("\n✅ Done! Your clips are saved in the 'clips/' folder.")
