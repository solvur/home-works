from pytube import YouTube
import uuid


def video(url):
        yt = YouTube(url)
        video_id = uuid.uuid4().fields[-1]
        yt.streams.filter(only_video=True).first().download(
                "vsakoe",f"{video_id}.mp4"
                                                            )
        return f"vsakoe/{video_id}.mp4"


def audio(url):
        yt = YouTube(url)
        audio_id = uuid.uuid4().fields[-1]
        yt.streams.filter(only_audio=True).first().download(
                "vsakoe",f"{audio_id}.mp3"
                                                            )
        return f"vsakoe/{audio_id}.mp3"


video("https://www.youtube.com/watch?v=vQPG70xSSo8&list=WL&index=17")
audio("https://www.youtube.com/watch?v=J---aiyznGQ&list=WL&index=213")
