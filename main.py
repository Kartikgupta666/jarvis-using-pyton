# pip install pyaudio

import pyttsx3 #pip install pyttsx4
import speech_recognition as sr #pip install speechRecognition
import datetime 
import os
import wikipedia
import pywhatkit
import pyautogui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Please tell me. what can I do??")       

def takeCommand():
   
    r = sr.Recognizer()
    
    # Increase energy threshold sensitivity
    r.energy_threshold = 300  # Default is 300, reduce to make it more sensitive
    r.dynamic_energy_threshold = True  # Auto-adjust based on ambient noise

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)  # Calibrate noise for 0.5 seconds
        r.pause_threshold = 0.6  # Shorter pauses for quicker response
        r.phrase_threshold = 0.3  # Minimum speaking duration
        r.non_speaking_duration = 0.3  # Silence before speech

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)  # Set limits
            print("Recognizing, please wait...")
            query = r.recognize_google(audio, language="en-IN")
            print(f"You said: {query}\n")
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start.")
            query = "none"
        except sr.UnknownValueError:
            print("Sorry, I could not understand.")
            query = "none"
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            query = "none"

        return query
        
    
if __name__ == '__main__':
    

  while True:
    query = takeCommand().lower()
    if 'wake up' in query: 
        wishMe()
        while True:
            query = takeCommand().lower()

            # time teller 

            if 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sir , The time is {strTime}")
        # browsers call back condations command
            
            elif 'microsoft edge' in query:
                speak("open MicroSoft edge")
                os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
            
            elif 'Brave' in query and 'search on brave' in query :
                speak("opening brave...")
                os.startfile("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")
            
        # search on browser
            
            elif "open" in query or "search" in query:
                query = query.replace("open" , "")
                pywhatkit.search(query)
                # pywhatkit.open(query)
                speak("done sir!!")
                    
            
            elif 'wikipedia' in query:
                speak("opening sir..")
                try:
                    query = query.replace("wikipedia" , "")
                    results = wikipedia.summary(query,sentences = 1)
                    speak("according to wikipedia")
                    print(results)
                    speak(results)
                except:
                    speak("no result found")
                    print("no result found")
                    
            elif 'play' in query :
                    query = query.replace("play" , "")
                    speak('playing' + query)
                    pywhatkit.playonyt(query)

                
            elif 'type' in query :
                speak("what should i write??")
                while True:
                    writeInNotepad = takeCommand()
                    if writeInNotepad == "exit typing":
                        speak("done sir")
                        break
                    else:
                        pyautogui.write(writeInNotepad) 
                #    attach notepad using osstartfile command using in edge also;
            elif 'exit' in query:
                speak("it's my pleasure to assist you..")
                speak("now im leaving !!")
                quit()
            elif 'break' in query:
                speak("Thanks sir!!")
                break
            
            # some intraction commands
            elif 'how are you' in query :
                speak("i'm fine thanks for asking.." )
                speak("how can i help you ??")
            elif 'who are you' in query or 'hu r u' in query :
                speak("i'm a virtual assistant " )
                speak("created by you ,  using python")
            elif 'what is your name' in query or "what's your name" in query :
                speak("my name is jarvis" )
                speak("how can i help you ??")
            elif 'its incorrect' in query or "it's incorrect" in query or 'glat hai' in query or 'its wrong' in query:
                speak("sorry sir.." )
                
            elif 'thanks' in query or 'cool' in query or 'thats nice' in query or "good job" in query :
                speak("its my pleasure" )
    else:
        print ("im sleepping")   
    