import tkinter
#erstellt ein kleines tkinter fenster
root = tkinter.Tk()
#gibt dem fenster einen Namen oder eine Überschrift je nachdem
root.title("Hello World")
#Gibt an dass die Größe des Fensters nicht verändert werden darf
root.resizable(0,0)
# Gibt die Hintergrundfarbe Blau an
root.config(bg="blue")
#Gibt die Größe des Fensters an also 400 mal 400 pixel
# root.geometry("400x400")
# bringt das tkinter Fenster in den Vollbildmodus
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
# erstellt ein Label das einen Text im Fenster root angibt mit dem Inhalt Hello world
label1 = tkinter.Label(root, text="hello world")
#gibt das label aus auf dem Fenster root
label1.pack(fill="y", expand="true")
#mainloop muss immer am Ende stehen
root.mainloop()