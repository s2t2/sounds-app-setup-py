from pprint import pprint
import speech_recognition as sr

client = sr.Recognizer()

with sr.Microphone() as mic:
    print("Say something!")
    audio = client.listen(mic)

transcript = client.recognize_google(audio)
#> 'how old is the Brooklyn Bridge'

response = client.recognize_google(audio, show_all=True)
pprint(response)