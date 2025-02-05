import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
# speaker.speak("joy boy has been return!")
speaker.speak("good morning")

speaker.speak("good bye")




    