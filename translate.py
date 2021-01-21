from translate import Translator
from termcolor import colored
import pyttsx3

words = str(input('Enter Words: '))
from_language = str(input('Enter The Source Language: '))
to_language = str(input('Enter The Goal Language: '))
voice_speech = str(input('Are You Want A Speech(y/n): '))

translator = Translator(from_lang=from_language, to_lang=to_language)
translation = translator.translate(words)

if voice_speech.lower() in ['y', 'yes']:
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()

print(f"From {from_language}: {words} --> To {to_language}: {translation}")
