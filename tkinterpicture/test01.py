#dieses Programm läuft nur wenn es über die Konsole ausgeführt wird manuell sonst gibt es eine Fehlermeldung
#this should be a little ui with an picture in it
# import tkinter as tk

import tkinter as tk
# importiert tinker als tk
from tkinter import PhotoImage
# import photoimage packet von tkinter um fotos darzustellen
programm = tk.Tk()
# erstellt ein fenster namens programm
logo = PhotoImage(file="C:/Users/lukas_paul/OneDrive/Dokumente/GitHub/python_tkinter/tkinterpicture/homer.gif")
# importiert foto 
label = tk.Label(programm, image=logo)
label.pack(side="top")
# weist foto ein paar eigenschaften zu 
programm.mainloop()
# main loop schleife muss immer am ende stehen
# aktualisiert das programm wärend der laufzeit