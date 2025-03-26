import os
import sys
import subprocess

# Get the script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define paths to yt-dlp and ffmpeg in the same directory
yt_dlp_path = os.path.join(script_dir, "yt-dlp.exe")
ffmpeg_path = os.path.join(script_dir, "ffmpeg.exe")

# Check if yt-dlp and ffmpeg exist in the same folder
if not os.path.exists(yt_dlp_path):
    print("Error: yt-dlp.exe not found in the script folder.")
    sys.exit(1)
if not os.path.exists(ffmpeg_path):
    print("Error: ffmpeg.exe not found in the script folder.")
    sys.exit(1)

# Get YouTube URL from user
video_url = input("Enter YouTube video URL: ").strip()

# Download all available subtitles using yt-dlp
print("Downloading all subtitles...")
subprocess.run([
    yt_dlp_path, "--write-subs", "--all-subs", "--skip-download", video_url
])

# Convert all .vtt files to .srt
for file in os.listdir(script_dir):
    if file.endswith(".vtt"):
        vtt_file = os.path.join(script_dir, file)
        srt_file = vtt_file.replace(".vtt", ".srt")

        print(f"Converting {vtt_file} to {srt_file}...")

        # Convert VTT to SRT using ffmpeg
        subprocess.run([ffmpeg_path, "-i", vtt_file, srt_file])

        # Delete the VTT file (optional)
        os.remove(vtt_file)

print("All subtitles downloaded and converted to .srt format.")
