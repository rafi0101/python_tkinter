import tkinter as tk
# from tkinter import *
import subprocess
from tkinter import messagebox 
# import tkMessageBox
programm = tk.Tk()
programm.geometry("640x480")
windowWidth = programm.winfo_reqwidth()
windowHeight = programm.winfo_reqheight()
positionRight = int(programm.winfo_screenwidth()/3.5 - windowWidth/3.5)
positionDown = int(programm.winfo_screenheight()/3.5 - windowHeight/3.5)

programm.geometry("+{}+{}".format(positionRight, positionDown))
programm.title("Games_Starter")
programm.iconphoto
programm.config(background="#4287f5")
programm.iconbitmap('C:/Users/lukas_paul/Downloads/battlefront.ico')
header = tk.Label(programm, font="arial", bg="#4287f5", text="Starten Sie Battlefront wenn sie klicken\n")
header.pack()
def battlefront():
    header1 = tk.Label(programm, text="\nBattlefront startet", bg="#4287f5")
    header1.pack()
button = tk.Button(programm, text='Start', width=25, command=battlefront)
button.pack()

programm.mainloop()
