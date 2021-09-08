from __future__ import annotations

import tkinter
from tkinter import *
from configparser import ConfigParser
import requests

def print_msg() -> None:
    label.config(text="Input: " + i.get(1.0, "end-1c"))
    label2.config(text="Input2: " + i.get(1.0, "end-1c"))

def create_api_file() -> None:
    """Create a file named config.ini in the current directory, and write
    the api key to it"""
    f = open("config.ini", "w")
    global key_name
    key_name = input("Enter key name:")
    f.write("[" + key_name + "]" + "\n")
    key = input("Enter key:")
    f.write("api=" + key)

window = Tk()
window.geometry("400x300")
window.title("My Weather App")

i = Text(window, height=1, width=30)
i.pack()

b = Button(window, text="Get Weather", command=print_msg)
b.pack()

label = Label(window, text="")
label.pack()

label2 = Label(window, text="")
label2.pack()

create_api_file()

c = ConfigParser()
c.read("config.ini")

api = c[key_name]['api']
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
window.mainloop()