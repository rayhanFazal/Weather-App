from __future__ import annotations
from typing import Tuple
import tkinter
from tkinter import *
from configparser import ConfigParser
import requests

# To get an API, go to https://openweathermap.org/, make an account, and then
# generate your own API, taking note of the API name and key. You can get the
# API from "Current Weather Data" APIs

def search_loc() -> None:
    """Search for the location entered by the user and output its weather info
    otherwise print an error."""
    loc = i.get(1.0, "end-1c")
    w_info = get_weather_info(loc)
    # Check if there is any info for the location
    if len(w_info) > 0:
        loc_label["text"] = "{} {}".format(w_info[0], w_info[1])
        temp_label["text"] = str(w_info[2]) + u"\N{DEGREE SIGN}" + "C"
        weather_label["text"] = w_info[3]
    else:
        print("Cannot find location: " + loc)

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
    return tuple()


window = Tk()
window.geometry("400x300")
window.title("My Weather App")

i = Text(window, height=1, width=30)
i.pack()

create_api_file()

c = ConfigParser()
c.read("config.ini")

api = c[key_name]['api'] # retrieve api key
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

b = Button(window, text="Get Weather", command=search_loc)
b.pack()
loc_label = Label(window, text="Location:")
loc_label.pack()
temp_label = Label(window, text="")
temp_label.pack()
weather_label = Label(window, text="")
weather_label.pack()

window.mainloop()