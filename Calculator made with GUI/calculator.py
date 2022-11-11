from logging import exception
from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())   
        else:
            try:
                value=eval(screen.get())
            except Exception as e: 
                print(e)
                scvalue.set("Error")
                screen.update()
                   
        scvalue.set(value)
        screen.update()

    elif text=="C":
        scvalue.set("")
        screen.update()

    elif text=="root":
        value=screen.get()/2
        scvalue.set(value)
        screen.update()       
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root=Tk()
root.geometry("500x500")
root.title("Deepak Calculator")
root.wm_iconbitmap("icon.gif")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue,font="lucida 40 bold")
screen.pack(ipadx=8,padx=10,pady=10)

f=Frame(root,bg="blue")
b=Button(f,text="7",bg="orange",padx=10,pady=10,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="8",bg="orange",padx=10,pady=10,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="9",bg="orange",padx=10,pady=10,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="C",bg="orange",padx=10,pady=10,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="OFF",bg="orange",padx=10,pady=10,font="lucida 30 bold",command=quit)
b.pack(side=LEFT,padx=10,pady=10)
f.pack()

f=Frame(root,bg="blue")
b=Button(f,text="4",bg="orange",padx=10,pady=10,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="5",bg="orange",padx=10,pady=10,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="6",bg="orange",padx=10,pady=10,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="=",bg="orange",padx=10,pady=10,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="+",bg="orange",padx=10,pady=10,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="blue")
b=Button(f,text="1",bg="orange",padx=10,pady=10,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="2",bg="orange",padx=10,pady=10,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="3",bg="orange",padx=10,pady=10,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="-",bg="orange",padx=10,pady=10,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="*",bg="orange",padx=10,pady=10,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="blue")
b=Button(f,text="0",bg="orange",padx=10,pady=10,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="00",bg="orange",padx=10,pady=10,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text=".",bg="orange",padx=10,pady=10,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="/",bg="orange",padx=10,pady=10,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="%",bg="orange",padx=10,pady=10,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="blue")
b=Button(f,text="^",bg="orange",padx=10,pady=10,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="%",bg="orange",padx=10,pady=10,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="/",bg="orange",padx=10,pady=10,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="root",bg="orange",padx=10,pady=10,font="lucida 30 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()
root.mainloop()