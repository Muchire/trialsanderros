from tkinter import*

count= 0
def click():
    global count
    count +=1
    print(count)

phone=Tk()

frame= Frame(phone,
             bg="light pink")
frame.pack()

Button(frame,text ="1",width = 3,bg="purple",command= click).pack(side= LEFT)
Button(frame,text ="2",width = 3,bg="light blue",command= click).pack(side= LEFT)
Button(frame,text ="3",width = 3,bg="light yellow",command= click).pack(side=LEFT)
Button(frame,text ="4",width = 3,command= click).pack()
Button(frame,text ="5",width = 3,command= click).pack()
Button(frame,text ="6",width = 3,command= click).pack()
Button(frame,text ="7",width = 3,command= click).pack()

phone.mainloop()