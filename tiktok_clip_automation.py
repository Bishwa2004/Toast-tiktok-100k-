# tiktok_clip_automation.py

from faster_whisper import WhisperModel
import subprocess
import os
import tempfile
import re

VIDEO_PATH = "TOAST.mp4"
MODEL_SIZE = "base"
DEVICE = "cpu"

# Step 1: Transcribe with timestamps per word
model = WhisperModel(MODEL_SIZE, device=DEVICE, compute_type="int8")
segments, info = model.transcribe(VIDEO_PATH, beam_size=5, word_timestamps=True)

print("\n🔍 Searching for highlight-worthy clips...")

# Step 2: Keyword detection
keywords = ["no way", "omg", "insane", "what just happened", "clip that", "holy", "crazy",
            "unbelievable", "he did it", "no shot", "i can't believe"]
highlight_segments = []
word_overlays = []

conversation_buffer = []
current_start = None
current_end = None
max_pause = 2.0

for segment in segments:
    if current_start is None:
        current_start = segment.start
    current_end = segment.end
    conversation_buffer.append(segment.text)

    lower_text = segment.text.lower()
    if any(k in lower_text for k in keywords):
        print(f"🔑 Keyword match: '{segment.text}'")
        highlight_segments.append((max(0, current_start - 1), current_end + 1))

        for word in segment.words:
            word_overlays.append((word.start, word.end, word.word))

        conversation_buffer = []
        current_start = None

if not highlight_segments:
    print("\n⚡ No transcript matches. Trying loudness-based detection using ffmpeg...")
    with tempfile.NamedTemporaryFile(delete=False) as temp_log:
        temp_path = temp_log.name

    ffmpeg_cmd = [
        "ffmpeg", "-i", VIDEO_PATH,
        "-af", "silencedetect=n=-30dB:d=0.5",
        "-f", "null", "-loglevel", "info", "-"
    ]

    with open(temp_path, "w") as log:
        subprocess.run(ffmpeg_cmd, stderr=log, stdout=subprocess.DEVNULL)

    with open(temp_path, "r") as log:
        lines = log.readlines()

    silence_ends = [float(m.group(1)) for line in lines if (m := re.search(r"silence_end: (\d+\.\d+)", line))]

    for ts in silence_ends:
        highlight_segments.append((max(0, ts - 2), ts + 4))

    print(f"\n✅ Found {len(highlight_segments)} audio-based highlight segments.")

# Step 4: Auto-clip with FFmpeg overlays
os.makedirs("clips", exist_ok=True)
font = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

for i, (start, end) in enumerate(highlight_segments):
    output = f"clips/clip_{i+1}.mp4"
    title = f"Highlight #{i+1}"

    base_filters = [
        f"crop=w='ih*9/16':h=ih:x='(in_w-out_w)/2':y='0'",
        f"smartblur=1.0:0.0",
        f"drawtext=fontfile='{font}':fontsize=48:fontcolor=white:borderw=2:bordercolor=black:x=(w-text_w)/2:y=50:text='{title}'",
        f"fade=t=in:st=0:d=0.3",
        f"fade=t=out:st={(end-start-0.3):.2f}:d=0.3",
        "setpts=0.75*PTS"
    ]

    # Stylized word-by-word subtitles
    for w_start, w_end, word in word_overlays:
        if w_start >= start and w_end <= end:
            color = "yellow" if word.strip().lower() in keywords else "white"
            fontstyle = f"drawtext=enable='between(t,{w_start-start:.2f},{w_end-start:.2f})':fontfile='{font}':fontsize=52:fontcolor={color}:borderw=4:bordercolor=black:text='{word.strip()}'"
            base_filters.append(fontstyle)

    vf = ",".join(base_filters)
    af = f"afade=t=in:st=0:d=0.3,afade=t=out:st={(end-start-0.3):.2f}:d=0.3,atempo=1.33"

    cmd = ["ffmpeg", "-ss", str(start), "-to", str(end), "-i", VIDEO_PATH,
           "-vf", vf, "-af", af,
           "-c:v", "libx264", "-crf", "23", "-preset", "fast", output]

    print(f"✂️ Clipping segment {i+1}: {start:.2f}s to {end:.2f}s ➝ {output}")
    subprocess.run(cmd)

print("\n🎉 Done! Stylized TikTok clips saved in 'clips/' folder.")
