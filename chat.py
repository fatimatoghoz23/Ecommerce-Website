import json
import os
import webbrowser
from asyncio import sleep

import pyaudio
import pywhatkit
import speech_recognition as sr
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render


def chatbotlisten(request):      
 try:
    dataa = json.loads(request.body)
    action = dataa['action']
    lis=sr.Recognizer()
    with sr.Microphone()as source:
      print('listen')
      voice=lis.listen(source)
      command=lis.recognize_google(voice)
      command = command.lower()
      print(command)
      webbrowser.register('chrome',None,
      webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"))
      if('samsung') in command:
        link='http://127.0.0.1:8000/search/?q=sumsung'
        webbrowser.get('chrome').open_new(link)
       
      elif('huawei') in command:
        link='http://127.0.0.1:8000/search/?q=huawei'
        webbrowser.get('chrome').open_new(link) 
      elif('infinix') in command:
        link='http://127.0.0.1:8000/search/?q=infinix'
        webbrowser.get('chrome').open_new(link) 
      elif('nokia') in command:
        link='http://127.0.0.1:8000/search/?q=nokia'
        webbrowser.get('chrome').open_new(link)
      elif('iphone') in command:
        link='http://127.0.0.1:8000/search/?q=iphone'
        webbrowser.get('chrome').open_new(link)
      else:
        link= 'http://127.0.0.1:8000/notfound/'
        webbrowser.get('chrome').open(link)
                
      print('Action:', action)        
      chatbotlisten(request)
      return render(request,'parts/chatbot.html',{})     
 # os.system('Notepad')    
 except json.decoder.JSONDecodeError:
      # 👇️ this runs
      print('The string does NOT contain valid JSON')
