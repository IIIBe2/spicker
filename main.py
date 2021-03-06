
import sys
import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
import subprocess

# настройки
opts = {
    "alias": ('андроид','анроед','дроид','андро','андроидок', 'android'),
    "tbr": ('скажи','расскажи','покажи','сколько','произнеси'),
    "cmds": {
        "ctime": ('текущее время','time','сейчас времени','который час', 'время'),
        "radio": ('включи музыку','radio','воспроизведи радио','включи радио'),
        "stupid1": ('расскажи анекдот','h2','рассмеши меня','ты знаешь анекдоты'),
        "rename": ('game'),
        "none": ('h1'),
        "pack1": ('набор один', 'набор адин')
    }
}

# функции
def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()

def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
        print("[log] Распознано: " + voice)
    
        if voice.startswith(opts["alias"]):
            # обращаются к Кеше
            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()
            
            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()
            
            # распознаем и выполняем команду
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")

def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    
    return RC

def execute_cmd(cmd):
    if cmd == 'none':
        os.system("C:\\Users\\artem\\Desktop\\rename.bat")
        restart()
        
    elif cmd == 'rename':
        os.system("C:\\Users\\artem\\Desktop\\rename.bat")

    elif cmd == 'pack1':
        os.system(path to browser)
        restart()

    elif cmd == 'radio':
        # воспроизвести радио
        os.system(path to radio)
        restart()
    
    elif cmd == 'stupid1':
        # рассказать анекдот
        speak("Мой разработчик не научил меня анекдотам ... Ха ха ха")
        restart()
    
    else:
        print('Команда не распознана, повторите!')

# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index = 1)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

# Только если у вас установлены голоса для синтеза речи!
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[4].id)

# forced cmd test
speak("...")

# speak("Добрый день, повелитель")
# speak("Кеша слушает")

def restart():
    os.system("C:\\Users\\artem\\Desktop\\Spiker.bat")
    sys.exit(0)

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.0) # infinity loop