from pprint import pprint
import speech_recognition as sr

print("STARTING THE APP")

client = sr.Recognizer()
print("CLIENT", type(client))

with sr.Microphone() as mic:
    print("MIC:", type(mic))
    print("Say something!")
    audio = client.listen(mic)
    print("AUDIO:", type(audio), dir(audio))

transcript = client.recognize_google(audio) #> unknownvalue error ... if not isinstance(actual_result, dict) or len(actual_result.get("alternative", [])) == 0: raise UnknownValueError()
print("TRANSCRIPT:", transcript)
