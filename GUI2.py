from tkinter import*
from tkinter import colorchooser

# def click():
#    color= colorchooser.askcolor()
#    print(color)
#    colorhex = color[1]
#    print(colorhex)
#    custom.config(bg=colorhex)
def save():
    notes= text.get("1.0",END)
    print(notes)

custom = Tk()
custom.geometry("400x400")
#
#
button= Button(text="save",
               command= save)
button.pack(side=BOTTOM)


text=Text(custom,
          bg="light blue",
          fg="purple",
          font=("Ink Free",15),
          padx=10,
          pady=10)
text.pack()

custom.mainloop()