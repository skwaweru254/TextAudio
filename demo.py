from gtts import gTTS
# pip install gtts
from playsound import playsound
# pip install playsound
audio = "audio.mp3"

language = 'en'

sp = gTTS(text="We are here", lang=language, slow=False)

sp.save(audio)

playsound(audio)
