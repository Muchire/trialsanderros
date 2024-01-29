from tkinter import*

count= 0
def click():
    global count
    count = count + 1
    # click = count

    print(count)

    if count ==1 :
        print("a")
    elif count ==2:
        print("b")
    elif count == 3:
        print("c")
    else:
        print(".")
    # print(click)


count = 0
def click1():
    global count
    count +=1
    # totalcount=
    # print(count)

    if count ==1 :
        print("d")
    elif count ==2:
        print("e")
    elif count == 3:
        print("f")
    else:
        print("g")
count=0
def click2():
    global count
    count +=1
    # totalcount=
    # print(count)

    if count ==1 :
        print("h")
    elif count ==2:
        print("i")
    elif count == 3:
        print("j")
    else:
        print("k")

def click3():
    global count
    count +=1
    # totalcount=
    # print(count)

    if count ==1 :
        print("l")
    elif count ==2:
        print("m")
    elif count == 3:
        print("n")
    else:
        print("o")

def click4():
    global count
    count +=1
    # totalcount=
    # print(count)

    if count ==1 :
        print("p")
    elif count ==2:
        print("q")
    elif count == 3:
        print("r")
    else:
        print("s")

def click5():
    global count
    count +=1
    # totalcount=
    # print(count)

    if count ==1 :
        print("t")
    elif count ==2:
        print("u")
    elif count == 3:
        print("v")
    else:
        print("w")

def click6():
    global count
    count +=1
    # totalcount=
    # print(count)

    if count ==1 :
        print("x")
    elif count ==2:
        print("y")
    elif count == 3:
        print("z")
    else:
        print("?")


def delete():
     button1.forget()



phone=Tk()

frame = Frame(phone,width= 300,height=300)
frame.place(x=200,y=0)
#
# frame= Frame(phone,width=500,
#              height=100,
#              bg="light pink"
#              )
# frame.pack()
# Label(frame,text="Phone").


button1=Button(frame,text ="1\na,b,c .",width = 6,bg="purple",command= click)
button1.grid(row=0,column=0)
Button(frame,text ="2\n d,e,f,g",width = 6,bg="light blue",command= click1).grid(row=0,column=1)
Button(frame,text ="3\nh,i,j,k",width = 6,bg="light yellow",command= click2).grid(row=0,column=2)
Button(frame,text ="4\nl,m,n,o",width = 6,bg="light yellow",command= click3).grid(row=1,column=0)
Button(frame,text ="5\np,q,r,s",width =6, bg="light yellow",command= click4).grid(row=1,column=1)
Button(frame,text ="6\nt,u,v,w",width = 6,bg="light yellow",command= click5).grid(row=1,column=2)
Button(frame,text ="7\nx,y,z ?",width = 6,bg="light yellow",command= click6).grid(row=2,column=0)

Button(frame,text ="delete",width = 6,bg="light yellow",command= delete).grid(row=2,column=1)


phone.mainloop()