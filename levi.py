from email.mime import audio
from fnmatch import translate
from logging import exception
from time import strftime
from unittest import result
from bs4 import BeautifulSoup
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import keyboard
from PyDictionary import PyDictionary as dict
from googletrans import Translator
import requests
import html
from pywikihow import search_wikihow 

 


engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',210)

def Speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def WishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Speak("Morning Sir")
        
    elif hour>=12 and hour<18:
        Speak("Afternoon Sir")
        
    else:
        Speak("Evening Sir")
        
    Speak("My name is Levi. How may I help you today")
    

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except exception as e:
        #print(e)
        
        print("Say that again please.....")
        return "none"
    
    return query


def Whatsapp():
     Speak("Tell me name of the person")
     name = takeCommand()
        
     if 'honey' in name:
            Speak("Tell me message sir")
            mesge=takeCommand()
            Speak("Tell me the time sir")
            Speak("Tell me the hour")
            hour=int(takeCommand())
            Speak("Tell me minutes")
            minut=int(takeCommand())
            pywhatkit.sendwhatmsg("+917974892261",mesge,hour,minut)
     elif 'papa' in name:
            Speak("Tell me message sir")
            mesge=takeCommand()
            Speak("Tell me the time sir")
            Speak("Tell me the hour")
            hour=int(takeCommand())
            Speak("Tell me minutes")
            minut=int(takeCommand())
            pywhatkit.sendwhatmsg("+919685127048",mesge,hour,minut)
           
           
def chrome():
    Speak("Chrome automation started")
    command=takeCommand()
    if 'close the current tab' in command:
        keyboard.press_and_release('ctrl+w')
    
    elif 'new tab' in command:
        keyboard.press_and_release('ctrl+t')
        
    elif 'downloads' in command:
        keyboard.press_and_release('ctrl+j')
        
    elif 'history' in command:
        keyboard.press_and_release('ctrl+h')
    elif 'pause' in command:
        keyboard.press('space')
        
        
def dictionary():
    Speak("Dictionary mode started")
    query=takeCommand()
    if 'meaning' in query:
        query=query.replace("what is the meaning of","")
        result=dict.meaning(query)
        print(result)
        Speak(f"Its meaning is{result}") 
        
    elif 'synonym' in query:
        query=query.replace("what is the synonym of","")
        result=dict.synonym(query)
        print(result)
        Speak(f"Its synonym is{result}") 
        
    elif 'opposite' in query:
        query=query.replace("what is the opposite of","")
        result=dict.antonym(query)
        print(result)
        Speak(f"Its opposite is{result}") 
    
    
def takeHindi():
    command=sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening......")
        command.pause_threshold=1
        audio=command.listen(source)  
        
    try:
        print("Recognising......")
        query=command.recognize_google(audio ,language='hi')
        print(query)
        
    except Exception as e:
        return "None"
    
    return query.lower()
    
    
def transeng():
     Speak("Tell me the line")
     line = takeHindi()
     traslate=Translator()
     result=traslate.translate(line)
     Text=result.text
     Speak(Text)
     

def temp():
    search="What is the temperature"
    url=f"https://www.google.com/search?q={search}"
    r=requests.get(url)
    data=BeautifulSoup(r.text,"html.parser")
    temperature=data.find("div", "BNeawe").text
    Speak("is is"+temperature+"celcius outside")
    

    
    
if __name__ == "__main__":
    WishMe()
    
    while True:
     query= takeCommand().lower()
     
     if 'wikipedia' in query:
         Speak("Searching in wikipedia.....")
         query=query.replace("wikipedia", "")
         results= wikipedia.summary(query,sentences=1)
         Speak("According to wikipedia")
         print(result)
         Speak(results)
         
     elif 'you need a break' in query:
         Speak("OK sir, Wake me up when u need me")
         break
    
    
     elif 'open scholarship' in query:
         webbrowser.open("http://scholarshipportal.mp.nic.in/MedhaviChhatra/Public/Track_Your_Application.aspx")
         
     
     elif 'play a song' in query:
         music_der="E:\mysongs"
         songs=os.listdir(music_der)
         print(songs)
         os.startfile(os.path.join(music_der,songs[0]))
     
    
     elif 'the time' in query:
         strtime= datetime.datetime.now().strftime("%H:%M:%S")
         Speak(f"Sir its {strtime}\n")
         
     elif 'how are you' in query:
         Speak("I am fine sir")
         
     elif 'search on youtube' in query:
         Speak("OK Sir this is what i found")
         query=query.replace("ok levi","")
         query=query.replace("search on youtube","")
         webbrowser.open("https://www.youtube.com/results?search_query="+query)
         
     elif 'google' in query:
         Speak("This is what i found Sir")
         query=query.replace("google","")
         query=query.replace("Levi","")
         pywhatkit.search(query)
         
     elif 'website' in query:
         Speak("OK Sir")
         query=query.replace("website","")
         web1=query.replace("open","")
         web2='https://www.' + web1 +'.com'
         webbrowser.open(web2)
        # print(web2)
        
     elif 'whatsapp' in query:
         Whatsapp()
       
     elif 'chrome automation' in query:
        chrome()
    
     elif 'repeat my words' in query:
        myword=takeCommand()
        Speak(myword)     
         
     elif 'dictionary' in query:
         dictionary()
         
     elif 'translator' in query:
         Speak("OK Sir you may speak the line now")
         transeng()
         
     elif 'temperature' in query:
         temp()
         
     elif 'how to' in query:
         Speak("Getting data from the internet")
         op=query.replace("Jarvis","")
         max_result = 1
         how_to_func=search_wikihow(op,max_result)
         assert len(how_to_func) == 1
         how_to_func[0].print()
         
        
     elif 'play' in query:
        song = query.replace('play', '')
        Speak('playing ' + song)
        pywhatkit.playonyt(song) 
    
         
