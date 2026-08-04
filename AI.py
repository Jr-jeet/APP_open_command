import speech_recognition as sr
import subprocess as sub

command= input("INPUT YOUR APP")
def open_app(command):
    if "pycharm" in command:
        sub.Popen(r"C:\Program Files\JetBrains\PyCharm 2025.3.1\bin\pycharm64.exe")
    
    elif "blender" in command:
        sub.Popen(r"C:\Program Files\Google\Play Games\Bootstrapper.exe")

    elif "chrome" in command:
        sub.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

open_app(command)
"""  """



    