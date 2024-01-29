from tkinter import *

vivan = Tk()
#
# vivan.geometry("300x300")
# vivan.title("first GUI ")
# vivan.config(background="pink") #or search hex colour picker and copy the code
# label=Label(vivan,text= "Hello There!",
#             font = ("Arial",10,"bold"),
#             fg = "gray",
#             bg="black")
# label.pack()
# label2 = Label(vivan,text = "How are you?")
# label2.place(x=100,y=30)
#
# count= 0
# def click():
#     global count
#     count +=1
#     print(count)
#     print("love you")
#
#
# button= Button(vivan,
#                text= "click me",
#                command= click,
#                font=("comic Sans",10),
#                fg="purple",
#                bg="pink")
#
# button.place(x=100,y=50)

# icon = PhotoImage(file="logo.jpg")
# vivan.iconphoto(True,icon)


# def submit():
#     username = entry.get()
#    print("Hello \n"+username+
#           "\nhow's your day going")
#
# # def delete():
#     entry.delete(0,END)
#
# def backspace():
#
#      entry.delete(len(entry.get())-1,END)
# #
# entry= Entry(vivan,
#              font= ("Arial",10),
#              bg= "purple",
#              fg="pink",
#              show="$")
# # entry.insert(1,"best",)
# entry.pack(side=RIGHT)
# #
# submit_button= Button(vivan,text="submit",
#                       command=submit,
#                       bg="purple")
# submit_button.pack(side=RIGHT)

# delete_button= Button(vivan,text="delete",
#                       command=delete,
#                       bg="purple")
# delete_button.pack(side=RIGHT)
#
# backspace_button= Button(vivan,text="backspace",
#                       command=backspace,
#                       bg="purple")
# backspace_button.pack(side=RIGHT)

# def display():
#     if(x.get()==1):
#         print("yaaay")
#     else:
#         print(":(")
#
#
#
# x = IntVar()
#
# # icon= PhotoImage(file = "Screenshot (11).png") images should be in png format
#
# check_button= Checkbutton(vivan,
#                           text="I agree",
#                           variable=x,
#                           onvalue=1,
#                           offvalue=0,
#                           command= display,
#                           bg="purple",
#                           fg="pink",
#                           image= icon,
#                           compound="left"
#                           )
# check_button.pack()

food = [ '🍚Rice','🍙Ugali','🥗Greens','🍘Beans','🍳Eggs']

def order():
    if(x.get()==0):
        print("you ordered rice")
    elif (x.get()==1):
        print("you ordered ugali")
    elif (x.get()==2):
        print("you ordered greens")
    elif (x.get()==3):
        print("you ordered beans")
    elif (x.get()==4):
        print("you ordered eggs")
    else :
        print("Sorry it's all we got")
# x=IntVar()
#
for index in range(len(food)):
   menu = Radiobutton(vivan,text = food[index],
                      variable=x,
                      font= ("Impact",20),
                      value=index,
                      bg="purple",
                      fg="pink",
                      command = order,
                      )
   menu.pack(anchor = "w")#lists the items downwards (side=LEFT) lists the items in a line
   menu.place(x=50,y=100)

# def done():
#     # global count
#     # count +=1
#     # print(count)
#    # print( listbox.get(listbox.curselection())) selection mode has changed
#
#    students=[]
#
#    for i in listbox.curselection():
#         students.insert(i,listbox.get(i))
#
#    for i in students:
#         print(i)
# def add():
#     listbox.insert(listbox.size(),entrybox.get())
#     listbox.config(height=listbox.size())
#
# def delete():
#     listbox.delete(listbox.curselection())
#
# listbox = Listbox(vivan,
#                   bg="purple",
#                   fg="pink",
#                   font=("Constantia",25),
#                   selectmode=MULTIPLE)
# listbox.pack()
#
#
# listbox.insert(1,"mark")
# listbox.insert(2,"john")
# listbox.insert(3,"luke")
# listbox.insert(4,"jane")
# listbox.insert(5,"ann")
#
#
# listbox.config(height=listbox.size())
# # count = 0
#
# entrybox = Entry(vivan)
# entrybox.pack()
#
# addbutton = Button(vivan,text="add missing name",
#                    command= add)
# addbutton.pack()
#
#
# deletebutton = Button(vivan,text="delete",
#                    command= delete)
# deletebutton.pack()
#
# donebutton= Button(vivan,text= "done",
#                    command= done )
# donebutton.pack()
#
#
vivan.mainloop()