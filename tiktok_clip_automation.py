# tiktok_clip_automation.py

from faster_whisper import WhisperModel
import subprocess
import os
import tempfile
import re

VIDEO_PATH = "TOAST.mp4"
MODEL_SIZE = "base"  # Options: tiny, base, small, medium, large-v2
DEVICE = "cpu"  # Use "cpu" for MacBook Air or no-GPU machines

# Step 1: Transcribe video with real-time output
model = WhisperModel(MODEL_SIZE, device=DEVICE, compute_type="int8")
segments, _ = model.transcribe(VIDEO_PATH, beam_size=5)

print("\n🔍 Searching for highlight-worthy clips...")

# Step 2: Find transcript-based highlight-worthy clips
keywords = ["no way", "omg", "insane", "what just happened", "clip that", "holy", "crazy",
            "unbelievable", "he did it", "no shot", "i can't believe"]
highlight_segments = []

for segment in segments:
    print(f"[TRANSCRIPT] {segment.start:.2f}s - {segment.end:.2f}s: {segment.text}")
    text = segment.text.lower()
    if any(k in text for k in keywords):
        start = max(0, segment.start - 3)
        end = segment.end + 3
        highlight_segments.append((start, end))

# Step 3: If no transcript hits, detect loud audio spikes
if not highlight_segments:
    print("\n⚡ No transcript matches. Trying loudness-based detection using ffmpeg...")
    with tempfile.NamedTemporaryFile(delete=False) as temp_log:
        temp_path = temp_log.name

    ffmpeg_cmd = [
        "ffmpeg",
        "-i", VIDEO_PATH,
        "-af", "silencedetect=n=-30dB:d=0.5",
        "-f", "null",
        "-loglevel", "info",
        "-"
    ]

    with open(temp_path, "w") as log:
        subprocess.run(ffmpeg_cmd, stderr=log, stdout=subprocess.DEVNULL)

    with open(temp_path, "r") as log:
        lines = log.readlines()

    silence_ends = []
    for line in lines:
        match = re.search(r"silence_end: (\d+\.\d+)", line)
        if match:
            silence_ends.append(float(match.group(1)))

    for i in range(len(silence_ends)):
        start = max(0, silence_ends[i] - 2)
        end = start + 6
        highlight_segments.append((start, end))

    print(f"\n✅ Found {len(highlight_segments)} audio-based highlight segments.")

# Step 4: Auto-clip with ffmpeg
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
    print(f"✂️ Clipping segment {i+1}: {start:.2f}s to {end:.2f}s ➝ {output_file}")
    subprocess.run(cmd)

print("\n🎉 Done! Your TikTok clips are saved in the 'clips/' folder.")

