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
from Levis import Ui_levi
from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import sys
from pyautogui import click


   
     
 

engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',210)


def Speak(audio):
        engine.say(audio)
        engine.runAndWait()
    

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        self.Taskgui()

    
   
    def WishMe(self):
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            Speak("Morning Sir")
            
        elif hour>=12 and hour<18:
            Speak("Afternoon Sir")
            
        else:
            Speak("Evening Sir")
            
        Speak("My name is Levi. How may I help you today")
        

    def takeCommand(self):
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


    def Whatsapp(self):
        Speak("Tell me name of the person")
        name = self.takeCommand()
            
        if 'honey' in name:
                Speak("Tell me message sir")
                mesge=self.takeCommand()
                Speak("Tell me the time sir")
                Speak("Tell me the hour")
                hour=int(self.takeCommand())
                Speak("Tell me minutes")
                minut=int(self.takeCommand())
                pywhatkit.sendwhatmsg("+917974892261",mesge,hour,minut)
        elif 'papa' in name:
                Speak("Tell me message sir")
                mesge=self.takeCommand()
                Speak("Tell me the time sir")
                Speak("Tell me the hour")
                hour=int(self.takeCommand())
                Speak("Tell me minutes")
                minut=int(self.takeCommand())
                pywhatkit.sendwhatmsg("+919685127048",mesge,hour,minut)
            
            
    def chrome(self):
        
            Speak("Chrome automation started")
            while True:
            
                command=self.takeCommand()
                
                if 'close the current tab' in command:
                    keyboard.press_and_release('ctrl+w')
                
                elif 'new tab' in command:
                    keyboard.press_and_release('ctrl+t')
                    
                elif 'downloads' in command:
                    keyboard.press_and_release('ctrl+j')
                    
                elif 'history' in command:
                    keyboard.press_and_release('ctrl+h')
            
                elif 'pause' in command:
                    keyboard.press('space bar')
                    
                elif 'skip' in command:
                    click(x=841, y=521)
                    
                elif 'exit' in command:
                    Speak("Exiting chrome automation")
                    break
            
            
    def dictionary(self):
        Speak("Dictionary mode started")
        query=self.takeCommand()
        if 'meaning' in query:
            self.query=self.query.replace("what is the meaning of","")
            result=dict.meaning(self.query)
            print(result)
            Speak(f"Its meaning is{result}") 
            
        elif 'synonym' in self.query:
            self.query=self.query.replace("what is the synonym of","")
            result=dict.synonym(query)
            print(result)
            Speak(f"Its synonym is{result}") 
            
        elif 'opposite' in self.query:
            self.query=self.query.replace("what is the opposite of","")
            result=dict.antonym(query)
            print(result)
            Speak(f"Its opposite is{result}") 
        
        
    def takeHindi(self):
        command=sr.Recognizer()
        with sr.Microphone() as source: 
            print("Listening......")
            command.pause_threshold=1
            audio=command.listen(source)  
            
        try:
            print("Recognising......")
            self.query=command.recognize_google(audio ,language='hi')
            print(self.query)
            
        except Exception as e:
            return "None"
        
        return self.query.lower()
        
        
    def transeng(self):
        Speak("Tell me the line")
        line = self.takeHindi()
        traslate=Translator()
        result=traslate.translate(line)
        Text=result.text
        Speak(Text)
        

    def temp(self):
        search="What is the temperature"
        url=f"https://www.google.com/search?q={search}"
        r=requests.get(url)
        data=BeautifulSoup(r.text,"html.parser")
        temperature=data.find("div", "BNeawe").text
        Speak("is is"+temperature+"celcius outside")
        

        
        
    if __name__ == "__main__":
        
        def Taskgui(self):
            self.WishMe()
            while True:
             self.query= self.takeCommand().lower()
            
             if 'wikipedia' in self.query:
                    Speak("Searching in wikipedia.....")
                    self.query=self.query.replace("wikipedia", "")
                    results= wikipedia.summary(self.query,sentences=1)
                    Speak("According to wikipedia")
                    print(result)
                    Speak(results)
                    
             elif 'you need a break' in self.query:
                    Speak("OK sir, Wake me up when u need me")
                    break
                
                
             elif 'open scholarship' in self.query:
                    webbrowser.open("http://scholarshipportal.mp.nic.in/MedhaviChhatra/Public/Track_Your_Application.aspx")
                    
                
             elif 'play a song' in self.query:
                    music_der="E:\mysongs"
                    songs=os.listdir(music_der)
                    print(songs)
                    os.startfile(os.path.join(music_der,songs[0]))
                
                
             elif 'the time' in self.query:
                    strtime= datetime.datetime.now().strftime("%H:%M:%S")
                    Speak(f"Sir its {strtime}\n")
                    
             elif 'how are you' in self.query:
                    Speak("I am fine sir")
                    
             elif 'search on youtube' in self.query:
                    Speak("OK Sir this is what i found")
                    self.query=self.query.replace("ok levi","")
                    self.query=self.query.replace("search on youtube","")
                    webbrowser.open("https://www.youtube.com/results?search_query="+self.query)
                    
             elif 'google' in self.query:
                    Speak("This is what i found Sir")
                    self.query=self.query.replace("google","")
                    self.query=self.query.replace("Levi","")
                    pywhatkit.search(self.query)
                    
             elif 'website' in self.query:
                    Speak("OK Sir")
                    self.query=self.query.replace("website","")
                    web1=self.query.replace("open","")
                    web2='https://www.' + web1 +'.com'
                    webbrowser.open(web2)
                    # print(web2)
                    
             elif 'whatsapp' in self.query:
                   self. Whatsapp()
                
             elif 'chrome automation' in self.query:
                    self.chrome()
                
             elif 'repeat my words' in self.query:
                    myword=self.takeCommand()
                    Speak(myword)     
                    
             elif 'dictionary' in self.query:
                    self.dictionary()
                    
             elif 'translator' in self.query:
                    Speak("OK Sir you may speak the line now")
                    self.transeng()
                    
             elif 'temperature' in self.query:
                    self.temp()
                    
             elif 'how to' in self.query:
                    Speak("Getting data from the internet")
                    op=self.query.replace("Jarvis","")
                    max_result = 1
                    how_to_func=search_wikihow(op,max_result)
                    assert len(how_to_func) == 1
                    how_to_func[0].print()
                    
                    
             elif 'play' in self.query:
                    song = self.query.replace('play', '')
                    Speak('playing ' + song)
                    pywhatkit.playonyt(song) 
             
                 
    
StartFunction=MainThread()

class Gui_start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.levi_ui=Ui_levi()     
        self.levi_ui.setupUi(self)
        
        self.levi_ui.Start.clicked.connect(self.Startfunc)
        self.levi_ui.pushButton.clicked.connect(self.close)
        
    def Startfunc(self):
        self.levi_ui.movies_label_2=QtGui.QMovie("goku.gif")
        self.levi_ui.label_2.setMovie(self.levi_ui.movies_label_2)
        self.levi_ui.movies_label_2.start()
        
        self.levi_ui.movies_label_3=QtGui.QMovie("loadas.gif")
        self.levi_ui.label_3.setMovie(self.levi_ui.movies_label_3)
        self.levi_ui.movies_label_3.start()
        
        self.levi_ui.movies_label_4=QtGui.QMovie("code.gif")
        self.levi_ui.label_4.setMovie(self.levi_ui.movies_label_4)
        self.levi_ui.movies_label_4.start()
        
        StartFunction.start()
        
        
        
Gui_app=QApplication(sys.argv)
Giu_levi=Gui_start()
Giu_levi.show()
exit(Gui_app.exec_())
        