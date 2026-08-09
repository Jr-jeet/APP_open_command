
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

import pandas as p 
# df=p.read_csv("himani  sem 2 addmission.pdf",encoding=latin1 / utf-8)
#(if error come then:-  then pass in encoding , utf-8  or latin1 )
# df=p.read_excel("himani  sem 2 addmission.pdf",encoding=latin1 / utf-8)
# df=p.read_json("himani  sem 2 addmission.pdf",encoding=latin1 / utf-8)
# print(df)              use for read data "what is in the data"
# gcsfs   if data in google cloude

# data ={


    
