import os
# import ffmpeg
import speech_recognition as sr

# import moviepy.editor

Path =  open(r'C:\Users\iDAFAdmin\Desktop\video conversion\tutorial.mp4')

#command for conversion from video to audio
command2mp3 = "ffmpeg -i tutorial.mp4 tutorial.mp3"
command2wav = "ffmpeg -i tutorial.mp3 tutorial.wav"

#execute video conversion commands

os.system(command2mp3)
os.system(command2wav)

#load wav file
r = sr.Recognizer()
with sr.AudioFile('tutorial.wav') as source:
     audio = r.record(source, duration=120) 
print(r.recognize_google(audio))

#path = os.path.dirname(os.path.abspath(__file__))