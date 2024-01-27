from tkinter import *
from tkinter import messagebox

van = Tk()

def click():
    messagebox.showinfo(title= "screw you",
                        message= "hahahaha")
    # while(True) :     # to ensure the messagebox doesnt stop poping up
    messagebox.showwarning(title="warning",
                        message="your'e screwed")
    messagebox.showerror(title="you fumbled",
                        message="hahahaha")
    if messagebox.askokcancel(title= "MARA TRIP",
                           message="Will you go with me"):
        print("Yaaaaaaay 🤗🤗🤗")
    else:
        print("It's okay I understand 😪😪😪")
    if messagebox.askretrycancel(title= "MARA TRIP",
                           message="Will you go with me"):
        print("Yaaaaaaay 🤗🤗🤗")
    else:
        print("It's okay I understand 😪😪😪")
     if messagebox.askyesno(title= "MARA TRIP",
                           message="Will you go with me"):
        print("Yaaaaaaay 🤗🤗🤗")
     else:
        print("It's okay I understand 😪😪😪")
     answer = messagebox.askquestion(title="MARA TRIP",
                           message="Will you go with me")
     if(answer == "yes"):
       print("I'd love to")
     else:
       print("No,thankyou")

   answer = messagebox.askyesnocancel(title="MARA MAYBE?", message="Will you come with?")
   if (answer==True):
    print("I'd love to")
   elif (answer == False):
    print("No,Thankyou")
   else:
    print("Had other plans in mind")
button = Button(van,command= click,
                text= "click me")
button.pack()

van.mainloop()
