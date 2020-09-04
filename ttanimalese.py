import sys, os

import functools

from pydub import AudioSegment

print(os.getcwd())

AudioSegment.converter = r"C:\\Users\\Luiz\\General Workspaces\\Python\\text_to_animalese\\ffmpeg"
#AudioSegment.ffmpeg = os.getcwd() + "\\ffmpeg\\ffmpeg.exe"
AudioSegment.ffprobe = "C:\\Users\\Luiz\\General Workspaces\\Python\\text_to_animalese\\ffmpeg\\ffprobe.exe"

text = "this is a test text"

silent = AudioSegment.silent(duration=300)

arr_sound = []

for letter in text:
    if letter == " ":
        arr_sound.append(silent)
    else:
        arr_sound.append(AudioSegment.from_mp3('./res/'+letter+'.mp3'))

result_animalese = functools.reduce(lambda a,b: a+b, arr_sound)
result_animalese.export('./test.mp3', format='mp3')
