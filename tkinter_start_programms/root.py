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
programm.title("Application_Starter")
programm.iconphoto
programm.config(background="#4287f5")
programm.iconbitmap('C:/Users/lukas/python_tkinter/tkinter_start_programms/assets/battlefront.ico')
header = tk.Label(programm, font="arial", bg="#4287f5", text="\n")
header.pack()
def programmieren():
    # header1 = tk.Label(programm, text="\nBattlefront startet", bg="#4287f5")
    # header1.pack()
    # subprocess.call(['C:/Program Files (x86)/Origin Games/STAR WARS Battlefront II/starwarsbattlefrontii.exe'])
    subprocess.call(['C:/Users/lukas/AppData/Local/Vivaldi/Application/vivaldi.exe'])
    subprocess.call(['C:/Users/lukas/AppData/Local/Programs/Microsoft VS Code/Code.exe'])
    # subprocess.call(['%SystemRoot%/system32/WindowsPowerShell/v1.0/powershell.exe'])
def battlefront():
    subprocess.call(['C:/Program Files (x86)/Origin Games/STAR WARS Battlefront II/starwarsbattlefrontii.exe'])
def rainbow():
    subprocess.call(["C:/Program Files (x86)/Steam/steamapps/common/Tom Clancy's Rainbow Six Siege/RainbowSix.exe"])
def warzone():
    subprocess.call(["C:/Program Files (x86)/Call of Duty Modern Warfare/Modern Warfare Launcher.exe"])
button = tk.Button(programm, text='Programmieren', width=25, command=programmieren)
button.pack()
header1 = tk.Label(programm, bg="#4287f5", text="\n")
header1.pack()
button1 = tk.Button(programm, text='Battlefront', width=25, command=battlefront)
button1.pack()
header2 = tk.Label(programm, bg="#4287f5", text="\n")
header2.pack()
button2 = tk.Button(programm, text='Rainbow', width="25", command=rainbow)
button2.pack()
header3 = tk.Label(programm, bg="#4287f5", text="\n")
header3.pack()
button3 = tk.Button(programm, text='warzone', width="25", command=warzone)
button3.pack()



programm.mainloop()
