from gtts import gTTS
from gtts.tokenizer.pre_processors import abbreviations, end_of_line
from pygame import mixer
import time

text = "Hello, this is a test of the Google Text-to-Speech API."
tts = gTTS(text=text, lang='en', slow=False, pre_processor_funcs=[abbreviations, end_of_line])

tts.save("output.mp3")

mixer.init()
mixer.music.load("output.mp3")
mixer.music.play()

time.sleep(10)  # Wait for the audio to finish playing
