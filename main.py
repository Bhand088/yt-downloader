import os
import yt_dlp
from pathlib import Path

download_dir = str(Path.home() / "Downloads")


urls = input("📥 Enter YouTube URLs (comma separated): ").split(",")


format_choice = input("🎞️ Choose format - (1) MP4 Video or (2) MP3 Audio: ")


ydl_opts = {
    "outtmpl": os.path.join(download_dir, "%(title)s.%(ext)s"),
    "progress_hooks": [lambda d: print_progress(d)]
}


if format_choice.strip() == "2":
    ydl_opts.update({
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192"
        }]
    })
else:
    ydl_opts["format"] = "18"  

# Progress bar hook function
def print_progress(d):
    if d["status"] == "downloading":
        print(f"⬇️  Downloading: {d['_percent_str']} {d['_speed_str']} ETA: {d['_eta_str']}", end="\r")
    elif d["status"] == "finished":
        print(f"\n✅ Download complete: {d['filename']}\n")


with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for url in urls:
        try:
            ydl.download([url.strip()])
        except Exception as e:
            print(f"\n❌ Error downloading {url.strip()}: {e}")
