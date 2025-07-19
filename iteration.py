from utils.voice_support import speak,listen
def human_feedback_loop(current_version):
    speak("Here is the current version.")
    print("\n==== CURRENT VERSION ====\n")
    print(current_version[:1000])
    speak("Do you approve this version? Say yes or no.")
    response=listen()
    if "yes" in response:
        speak("Version approved.")
        return current_version, True
    elif "no" in response:
        speak("Please dictate your improved version.")
        revised=listen()
        if revised:
            speak("Using your revised version.")
            return revised, False
        else:
            speak("No revision heard. Keeping current version.")
            return current_version, False
    else:
        speak("I did not understand. Keeping current version.")
        return current_version, False