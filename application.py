import speech_recognition as sr
import os
import data_base

exe_keywords = data_base.execution_keyword
list_program = data_base.list_program


def hear():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        audio = mic.listen(source)

    try:
        # The language defined is pt-br, change this to your language
        # don't forget to change the execution_keywords in data_base
        phrase = mic.recognize_google(audio, language='pt-BR')
        list_word = phrase.split(' ')
        print(list_word)

        for keyword in exe_keywords:
            for word in list_word:
                if word == keyword:
                    for program in list_word:
                        for list_p in list_program:
                            if program == list_p:
                                print(program)
                                os.system(f'start {program}')
                                break
        print('No execution trigger detected')
        print(phrase)
    except:
        print("Silence or voice don't detected")


while True:
    hear()
