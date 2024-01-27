from tkinter import*
from tkinter import filedialog

window = Tk()

def openfile():
    filepath=filedialog.askopenfilename(filetypes=(("all files","*.*"),("text files","*.txt")))
    file=open(filepath,"rt")
    print(file.read())
    file.close()
button= Button(window,
               text= "Open",
               command = openfile
               )
button.pack()
window.mainloop()