import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Adjusting for ambient noise... Please wait...")
    r.adjust_for_ambient_noise(source, duration=1)
    print("Say something:")
    audio=r.listen(source)
try:
    text=r.recognize_google(audio)
    print("You said: "+text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))