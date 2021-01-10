import onetimepad
from tkinter import *



root = Tk()
root.title("Chryptography App")

def encryptMessage():
    a = var.get()
    
    ct = onetimepad.encrypt(a,"shiva")
    print("Working",ct) 
    
    e2.delete(0,END)
    e2.insert(END,ct)

def dycrptMessage():
    a = var2.get()
    ct = onetimepad.decrypt(a,"shiva")
    print("Working",ct) 
    
    e4.delete(0,END)
    e4.insert(END,ct)
    
    
    
l1 = Label(root,text="Plain Text")
l1.grid(row=0,column=0)


l3 = Label(root,text="Encypted Text")
l3.grid(row=0,column=2)

var= StringVar()
e1 = Entry(root,textvariable=var)
e1.grid(row=0,column=1)

var2= StringVar()
e3 = Entry(root,textvariable=var2)
e3.grid(row=0,column=3)



l2 = Label(root,text="Encypted Text")
l2.grid(row=1,column=0)

l4 = Label(root,text="Plain Text")
l4.grid(row=1,column=2)


e2 = Entry(root)
e2.grid(row=1,column=1)

e4 = Entry(root)
e4.grid(row=1,column=3)

b1 = Button(root,text="Encyption",bg="blue",fg="Red",command=encryptMessage)
b1.grid(row=2,column=1)

b2 = Button(root,text="Dycrption",bg="blue",fg="Red",command=dycrptMessage)
b2.grid(row=2,column=3)




root.mainloop()
