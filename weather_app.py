from __future__ import annotations

import tkinter
from tkinter import *
from configparser import ConfigParser
import requests

def print_msg() -> None:
    label.config(text="Input: " + i.get(1.0, "end-1c"))
    label2.config(text="Input2: " + i.get(1.0, "end-1c"))

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

window.mainloop()