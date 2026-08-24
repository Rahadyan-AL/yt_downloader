import shutil

import yt_dlp

url = input("Enter the URL of the video: ")
ffmpeg_available = shutil.which("ffmpeg") is not None
format_selector = "bestvideo+bestaudio/best" if ffmpeg_available else "best"

yt_dlp.YoutubeDL(
    {"format": format_selector}
).download([url])