import os
from pytube import YouTube
from os import path
from pydub import AudioSegment


def downloadVideo(file):
    with open(file) as f:
        line = f.readline().strip()
        while line != "":
            yt = YouTube(line)
            video = yt.streams.filter(only_audio=True).first()
            out = video.download()

            line = f.readline().strip()


def convertToWav(src, dst):
    sound = AudioSegment.from_file(src, format="mp4")
    sound.export(dst, format="wav")


def bundle():
    pass
    # bundle everything together


def getTranscript(file):
    with open(file) as f:
        line = f.readline().strip()
        while line != "":
            pass

# downloadVideo("downloadFile.txt")
# convertToWav(f"{os.getcwd()}/audio1.mp4", f"{os.getcwd()}/audio1.wav")
#