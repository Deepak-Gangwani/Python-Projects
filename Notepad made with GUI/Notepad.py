from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfile, asksaveasfilename
import tkinter.messagebox as tmsg
import os

def myfunc():
    pass

def newFile():
    global file
    root.title("Untitled-Notepad")
    file=None

def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])    
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])        
        if file=="":
            file=None
        else:
            #Save as a new file
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"-Notepad")
            print("File Saved")
    else:
        #save the file
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>")) 

def paste():
    TextArea.event_generate(("<<Paste>>")) 

def about():
    showinfo("About Notepad","Notepad Made By Mr.Deepak Gangwani.")

def quitApp():
    value=tmsg.askquestion("Do you really want to leave?","If you want to quit from this file click on yes otherwise no!")          
    if value=="yes":
        msg=quit()
    else:
        pass  


if __name__=="__main__":
    #basic tkinter setup
    root=Tk()
    root.title("Untitled-Notepad")
    root.wm_iconbitmap("pic1.jpeg")
    root.geometry("644x788")

    #Add text Area
    TextArea=Text(root,font="lucida 13 bold")
    file=None
    TextArea.pack(expand=True,fill=BOTH)

    #Lets create a menubar
    MenuBar=Menu(root)
    
    #FileMenu starts 
    FileMenu=Menu(MenuBar,tearoff=0)
    #To open new file
    FileMenu.add_command(label="New",command=myfunc)
    FileMenu.add_command(label="New Window",command=myfunc)
    #To open already exiting file
    FileMenu.add_command(label="Open...",command=openfile)
    #To save the current file
    FileMenu.add_command(label="Save",command=savefile)
    FileMenu.add_command(label="Save As",command=savefile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Page Setup",command=myfunc)
    FileMenu.add_command(label="Print",command=myfunc)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApp)
    root.config(menu=MenuBar)
    MenuBar.add_cascade(label="Files",menu=FileMenu)

    #Edit Menu Start
    EditMenu=Menu(MenuBar,tearoff=0)
    EditMenu.add_command(label="Undo",command=myfunc)
    EditMenu.add_separator()
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)
    EditMenu.add_command(label="Delete",command=myfunc)
    EditMenu.add_separator()
    EditMenu.add_command(label="Search with Bing...",command=myfunc)
    EditMenu.add_command(label="Find...",command=myfunc)
    EditMenu.add_command(label="Find Next",command=myfunc)
    EditMenu.add_command(label="Find Previous",command=myfunc)
    EditMenu.add_command(label="Replace",command=myfunc)
    EditMenu.add_command(label="Go To...",command=myfunc)
    EditMenu.add_separator()
    EditMenu.add_command(label="Select All",command=myfunc)
    EditMenu.add_command(label="Time/Date",command=myfunc)
    MenuBar.add_cascade(label="Edit",menu=EditMenu)
    
    #Format menu start
    FormatMenu=Menu(MenuBar,tearoff=0)
    FormatMenu.add_command(label="Word Wrap",command=myfunc)
    FormatMenu.add_command(label="Font",command=myfunc)
    MenuBar.add_cascade(label="Format",menu=FormatMenu)

    #View Menu start
    ViewMenu=Menu(MenuBar,tearoff=0)
    ViewMenu.add_command(label="Zoom",command=myfunc)
    ViewMenu.add_command(label="Status Bar",command=myfunc)
    MenuBar.add_cascade(label="View",menu=ViewMenu)
    
    #Help Menu Start
    HelpMenu=Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="View Help",command=myfunc)
    HelpMenu.add_command(label="Send Feedback",command=myfunc)
    HelpMenu.add_separator()
    HelpMenu.add_command(label="About Notepad",command=about)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)

    root.config(menu=MenuBar)

    #Adding scroll bar using rules
    scroll=Scrollbar(TextArea)
    scroll.pack(side=RIGHT,fill=BOTH)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll.set)


    
root. mainloop()