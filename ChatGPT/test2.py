import speech_recognition as sr
import openai  
import pyttsx3
import os
import re
import webbrowser
import datetime


openai.api_key = "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"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



# Buat fungsi untuk mengakses API ChatGPT
def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    message = response.choices[0].text.strip()
    return message

def myCommand():
    "listens for commands"
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language='id-ID').lower()
        print('You : ' + command + '\n')
        text = generate_text(command)
        print("Bot: ",text)

        engine.say(text)
        engine.runAndWait()


    except sr.UnknownValueError:
        print('Bot : Your last command couldn\'t be heard')
        command = myCommand();

    return command


#loop to continue executing multiple commands
while True:
    myCommand()
    
