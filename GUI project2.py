from tkinter import *
from tkinter import ttk

key = Tk()

notebook= ttk.Notebook(key)  #manages multiple window displays

tab1= Frame(notebook)
tab2= Frame(notebook)
tab3= Frame(notebook)

notebook.add(tab1,text="1")
notebook.add(tab2,text="2")
notebook.add(tab3,text="3")

notebook.pack(expand=True,fill="both")

Label(tab1,text="write suggestions",width=50,height=50).pack()

Label(tab2,text="write sugg",width=50,height=50).pack()

Label(tab3,text="write s",width=50,height=50).pack()
key.mainloop()