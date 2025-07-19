import speech_recognition as sr
import pyttsx3
recognizer=sr.Recognizer()
engine=pyttsx3.init()
engine.setProperty("rate",150)
recognizer.energy_threshold=300
recognizer.dynamic_energy_threshold=True
def speak(text):
    print(f"[Voice] {text}")
    engine.say(text)
    engine.runAndWait()
def listen(timeout=10,phrase_time_limit=5):
    try:
        with sr.Microphone() as source:
            speak("Listening...")
            print("[Voice] Calibrating mic for ambient noise...")
            recognizer.adjust_for_ambient_noise(source,duration=1)
            audio=recognizer.listen(source,timeout=timeout,phrase_time_limit=phrase_time_limit)
            text=recognizer.recognize_google(audio)
            print(f"[User said] {text}")
            return text.lower()
    except sr.WaitTimeoutError:
        speak("I didn't hear anything. Please respond quicker next time.")
        return ""
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Speech Recognition service is unavailable.")
        return ""
    except Exception as e:
        print(f"[Error] {e}")
        return ""