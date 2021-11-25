import pyttsx3#module to take voice
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
#to speak the jarvis
def speak(audio):
    engine=pyttsx3.init('sapi5')#it is an api given by the window used to take voice as input or we can use the inbuilt voice of the window.
    voices=engine.getProperty("voices")
# print(voices)
    engine.setProperty("voices",voices[1].id) #to get the voice id set in the system 
    engine.setProperty("rate",188)
    # print(voices[0].id) 
    # print(voices[1].id)
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("good morning sir")

    elif hour >= 12 and hour<15:
        speak("good afternoon sir")
    elif hour >=15 and hour <=21:
        speak("good evening sir")

    else:
        speak("good night sir")
    speak("how may i help u ")

def takecommand(): #it will take microphone input from the user and will return string output
    r=sr.Recognizer() #it will help to recognise the audio
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold=1 #goto defination to look into it.
        r.energy_threshold=500
        audio=r.listen(source)

    try:
        print("recoginising....")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said :{query}\n")
    except Exception as e:
        print(e)
        print("say that again please....")
        return "none"
    return query

if __name__=="__main__":
    # speak("daulat is a good boy")
    # speak("hello sir , how are you")
    # wishme()
    while True:
        query=takecommand().lower()
        if "about" in query:
            speak("searching wikipedia....")
            query=query.replace("about","")
            results=wikipedia.summary(query,sentences=2)
            speak("acording to wikipedia ..")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        elif "open instagram" in query:
            webbrowser.open("instagram.com")
        elif "play music" in query:
            webbrowser.open("music.com")
        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir , the time is {strTime}")
        elif "open code" in query:
            codepath="C:\\Users\\win10\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
