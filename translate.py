import requests
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import json
from loguru import logger


logger.add("translate_logs.log", format="{time} | {level} | {message}", rotation="100MB") # Adds a file in which logs are stored

url = "https://google-translate1.p.rapidapi.com/language/translate/v2" # Makes the url to which the text is translated

root = tk.Tk()

language = [
    "ru",
    "en",
] # Makes a list of languages

source = StringVar() # Makes it appear in the drop menu
source.set(language[0]) # Makes so that only the first language from the list of languages ​​is displayed in the drop menu

drop = OptionMenu(root, source, *language) # Makes a drop menu
drop.place(x = 1, y = 20)
labeldrop = tk.Label(root, text = "What language do you want to translate into?") # Makes a label with the name drop menu
labeldrop.place(x = 1, y = 1)

target = StringVar() # Makes it appear in the drop menu
target.set(language[0]) # Makes so that only the first language from the list of languages ​​is displayed in the drop menu

drop1 = OptionMenu(root, target, *language) # Makes a drop menu
drop1.place(x = 1140 , y = 20)
labeldrop = tk.Label(root, text = "Which language do you want to translate from?") # Makes a label with the name drop menu
labeldrop.place(x = 1012, y = 1)

textwidgets_frm = tk.Frame(relief = tk.SUNKEN, borderwidth=3) # Make a window
textwidgets_frm.pack()

translation_lbl = tk.Label(master = textwidgets_frm, text="Enter:") # Makes the text where it is said to be displayed
translation_lbl.grid(row=0, column=0)
translation_ent = tk.Entry(master = textwidgets_frm, width=50) # Makes a text for input that will be translated
translation_ent.grid(row=0, column=1)


def translate_text():
	sourcetranslate = source.get()
	targettranslate = target.get()
	translation = translation_ent.get() 
	if translation_ent.get() != '':
		payload = {
			"q":"{}".format(translation),
			"source": "{}".format(sourcetranslate),
			"target": "{}".format(targettranslate),
		} # Uses url for translation and binds drop menu

		headers = {
 			"content-type":"application/json",
 			"X-RapidAPI-Key":"f0eda7c17amsha10f3c793fdf668p1ba57fjsn4b46df9be184",
 			"X-RapidAPI-Host":"deep-translate1.p.rapidapi.com"
		} # Translates the text
		response = requests.request("POST", url, json=payload, headers=headers) # Goes to url and translates
		json = response.json() # Makes with Jason's shift a shift

		text_translate = json['data']['translations']['translatedText'] # It is addressed by these keys
		translated_text.config(text="Translated text: {}".format(text_translate)) # Inserts the translated text
	else:
		messagebox.showerror('Error', 'Line is empty') # Returns an empty string error


translated_text = tk.Label(
    text="",
    bg="white", 
    fg="black"
) # Creates a label where the translated text is inserted
translated_text.pack()

frm_buttons = tk.Frame() # Make a window
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

translate_btn = tk.Button(master = frm_buttons, text = "Translate", command = translate_text) # Makes a button that translates the text
translate_btn.pack(padx=10, ipadx=10)

logger.info("Everything is good") # Makes a log that shows that everything is fine

root.mainloop()