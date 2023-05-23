# Copyright 2022 Samuel Ruairi Bullard

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

        #http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

import PySimpleGUI as sg
import os.path
from os.path import exists

# Sets the GUI theme
sg.change_look_and_feel('SystemDefaultForReal')

# Sets the window title
title = "BullDozer - Author: Samuel Bullard, Github: abullard1"

# Gets the .exe path if the program is run from an exe
if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
elif __file__:
        application_path = os.path.dirname(__file__)

# Gets the relative path of the OC.png image from the exe resources
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Checks if the OCZEILE1 and OCZEILE2 Text files exist already
OC1_exists = exists(application_path+'\\OCZEILE1.txt')
OC2_exists = exists(application_path+'\\OCZEILE2.txt')

# Reads the OCZEILE1 or OCZEILE2 files if they exist
def readIfOCFileExists(OCNumber):
    if OCNumber == 1 and OC1_exists:
        with open(application_path+'\\OCZEILE1.txt', "r") as file:
            numberOC1 = file.read()
        return numberOC1
    if OCNumber == 2 and OC2_exists:
        with open(application_path+'\\OCZEILE2.txt', "r") as file:
            numberOC2 = file.read()
            return numberOC2
    else:
        return

# Column of Text and Input fields
col_layout = [
    [sg.Text("Auftragsspezifische Nummer", background_color="white")],
    [sg.Input(readIfOCFileExists(1), size=(20, 1), background_color="#f2f2f2")],
    [sg.Text("Fortlaufende Nummer", background_color="white")],
    [sg.Input(readIfOCFileExists(2), size=(20, 1), background_color="#f2f2f2")]
]

# Column of Text and Input fields with the save and exit buttons
col_layout_elements = [
    [sg.Column(col_layout, expand_x=False, background_color="white")],
    [sg.Button("Save", pad=20, size=(10, 1), button_color="SlateBlue1"), sg.Button("Exit", pad=20, size=(10, 1), button_color="IndianRed1")],
]

# Frame layout made up of Column of Text and Input fields with the save and exit buttons
frame_layout = [
    sg.Frame(title=None, layout=col_layout_elements, border_width=5, background_color="white", element_justification="center")
]

# Layout, made up of the frame layout aswell as a descriptive image, which is passed to the GUI Window below
layout = [
    [frame_layout, sg.Image(filename=resource_path("OC.png"))]
]

# Sets the image to be displayed
window = sg.Window("BullDozer", layout=layout, background_color="white", margins=(25, 20), element_justification="c", font=("Arial", 12))

# Loop reading events and values of input fields
while (True):
    event, values = window.read()

    # Closes the program if the exit button is clicked
    if (event == sg.WIN_CLOSED or event == "Exit"):
        break

    # Saves the input values to .txt files in the same directory of the program and closes the program
    if (event == "Save"):
        OC1 = open("OCZEILE1.txt", "w")
        OC1.write(str(values[0]))
        OC1.close()
        OC2 = open("OCZEILE2.txt", "w")
        OC2.write(str(values[1]))
        OC2.close()
        window.close()

window.close()

