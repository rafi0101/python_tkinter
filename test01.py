<<<<<<< HEAD
#this should be a little ui with an picture in it
# import tkinter as tk

import tkinter as tk
# importiert tinker als tk
from tkinter import PhotoImage
# import photoimage packet von tkinter um fotos darzustellen
programm = tk.Tk()
# erstellt ein fenster namens programm
logo = PhotoImage(file="homer.gif")
# importiert foto 
label = tk.Label(programm, image=logo).pack(side="top")
# weist foto ein paar eigenschaften zu 
programm.mainloop()
# main loop schleife muss immer am ende stehen
# aktualisiert das programm wärend der laufzeit
=======
>>>>>>> 09d42a44dc31b815ff7d59ad93a5f8f605186881

