from __future__ import annotations
from typing import Tuple
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

def get_weather_info(location: str) -> tuple:
    """Return a tuple containing the city, country, temperature, and weather
    of <location>"""
    info = requests.get(url.format(location, api))
    if info:
        j = info.json()
        # retrieve necessary info from json file <j>
        city = j["name"]
        country = j["sys"]
        temp = j["main"]["temp"] - 273.15 # convert kelvin to celsius
        w = j["weather"][0]["main"]
        return (city, country, temp, w)
    print("Unable to retrieve info for location " + location)


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

api = c[key_name]['api'] # retrieve api key
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

get_weather_info(i.get(1.0, "end-1c"))

window.mainloop()