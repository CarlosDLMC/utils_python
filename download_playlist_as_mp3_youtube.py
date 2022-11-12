import re
from pytube import Playlist
from youtube_dl import YoutubeDL

OPTIONS = {
    'format': 'bestaudio',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}

playlist = Playlist("https://www.youtube.com/playlist?list=PLNQxFJxo5FJRr7a1QqDAdhw0d4txjVLNh")
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

audio_downloder = YoutubeDL(OPTIONS)

for song in playlist:
    audio_downloder.extract_info(song)
