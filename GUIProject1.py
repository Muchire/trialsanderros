from tkinter import *
from tkinter import filedialog

stick = Tk()
def create_note():
    new_note = Tk()
def savefile():
    file= filedialog.asksaveasfile(initialdir="C:\\Users\\user\\PycharmProjects\\trialsanderros",
                                   defaultextension=".txt",
                                   filetypes=[("Text file",".txt"),
                                   ("html",".html"),
                                   ("all files",".txt")])
    notes= str(text.get("1.0",END))
   # notes = input("write anything") # you can imput on the window consel
    file.write(notes)
    file.close

button = Button (text= "save",command= savefile)
button.pack()

Button(stick,text="new note",command= create_note,width=10).pack(side=BOTTOM)

text=Text(stick,
          bg= "light yellow")
text.pack()

stick.mainloop()
