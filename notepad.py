from tkinter import*
from tkinter import colorchooser
from tkinter import filedialog

def click():
   color= colorchooser.askcolor()
   print(color)
   colorhex = color[1]
   print(colorhex)
   custom.config(bg=colorhex)
def save():
    notes= text.get("1.0",END)
    filedialog.asksaveasfile( filetypes=[
        ("text files",".txt"),
        ("all files",".*"),
    ])
    print(notes)

def new ():
    new_page=Tk()
    new_page.geometry("300x400")
    new_page.title("MY NOTES 😀😀")
    def click():
        color = colorchooser.askcolor()
        print(color)
        colorhex = color[1]
        print(colorhex)
        new_page.config(bg=colorhex)



    button= Button(new_page,text="save",
                    command=save,bg= "pink",fg="purple")
    button.pack(side=BOTTOM)

    button1 = Button(new_page,text="new page",
                     command=new,bg= "pink",fg="purple")
    button1.pack(side=TOP)

    button2 = Button(new_page,text="change theme",
                     command=click,bg= "pink",fg="purple")
    button2.pack(side=TOP)

    label = Label(new_page, text="FIND WHAT YOU NEED?😀",
                  font=("Arial", 10, "bold"),
                  fg="black",
                  )
    label.pack()

custom = Tk()
custom.geometry("400x400")
custom.title("MY NOTES 😀😀")
label=Label(custom,text= "HOW YOU DOING?😏",
            font = ("Arial",10,"bold"),
            fg = "black",
           )
label.pack()

button= Button(text="save",
               command= save,
               bg= "pink",fg="purple")
button.pack(side=BOTTOM)

button1= Button(text="new page",
               command= new,bg= "pink",fg="purple")
button1.pack(side=TOP)

button2= Button(text="change theme",
               command= click,bg= "pink",fg="purple")
button2.pack(side=TOP)



text=Text(custom,
           bg= "light yellow",
          fg="purple",
          font=("Ink Free",15),
          padx=10,
          pady=10)
text.pack()

custom.mainloop()