from gtts import gTTS
from playsound import playsound
'''
text = "Hello there"
sound = gTTS(text)
sound.save("test.mp3")
playsound("test.mp3")
'''
from TTS.api import TTS
import pygame

text = "Hello, this is Coqui TTS speaking offline."

# Load a small model (works on 4GB RAM)
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

# Generate audio file
tts.tts_to_file(text=text, file_path="voice.wav")

# Play using pygame
pygame.mixer.init()
pygame.mixer.music.load("voice.wav")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass
'for python3.10 only\'