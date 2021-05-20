import os
import ffmpeg
import speech_recognition as sr

import moviepy.editor

Path =  r'C:\Users\iDAFAdmin\Desktop\video conversion\tutorial.mp4'

#command for conversion from video to audio
command2mp3 = "ffmpeg -i Path Bolna.mp3"
command2wav = "ffmpeg -i Bolna.mp3 Bolna.wav"

#execute video conversion commands

os.system(command2mp3)
os.system(command2wav)

#load wav file
r = sr.Recognizer()
with sr.AudioFile('Bolna.wav') as source:
     audio = r.record(source, duration=120) 
print(r.recognize_google(audio))