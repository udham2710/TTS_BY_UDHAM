import speech_recognition as sr
import os
import threading

from mtranslate import translate

from colorama import Fore,Style,init

init(autoreset=True)

def print_loop():
    while True:
        print(Fore.GREEN + "I am Listening",end="",flush=True)
        print(Style.RESET_ALL,end="",flush=True)
        
        
def translate_hindi_to_english(text):
    english_text = translate(text , "en-in")
    return english_text

def speech_to_text_python():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 34000
    recognizer.dynamic_energy_adjustment_damping