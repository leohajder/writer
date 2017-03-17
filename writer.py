from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

filename = None
saved = True

def fNew(*args):
    global filename, saved
    if(saved == False):
        save = promptToSave()
        if(save == True):
            fSave()
        elif(save == None):
            return
    filename = None
    text.delete(0.0, END)
    saved = True
    
def fOpen(*args):
    global filename, saved
    if(saved == False):
        save = promptToSave()
        if(save == True):
            fSave()
        elif(save == None):
            return
    try:
        f = filedialog.askopenfile(filetypes = [('text files', '.txt'),('all files', '.*')])
        if(f):
            filename = f.name
            t = f.read()
            text.delete(0.0, END)
            text.insert(END, t)
            saved = True
    except:
        messagebox.showerror("Error", "Unable to open file.")
      
def fSave(*args):
    global filename, saved
    t = text.get(0.0, END)
    if(filename):
        f = open(filename, "w")
        f.write(t)
        f.close()
        saved = True
    else:
        fSaveAs()

def fSaveAs(*args):
    global saved
    f = filedialog.asksaveasfile(defaultextension=".txt", filetypes = [('text files', '.txt'),('all files', '.*')])
    t = text.get(0.0, END)
    if(f):
        try:
            f.write(t)
            f.close()
            saved = True
        except:
            messagebox.showwarning("Error", "Unable to save file.")

def onExit(*args):
    global saved
    if(saved == False):
        save = promptToSave()
        if(save == True):
            fSave()
        elif(save == None):
            return
    app.destroy()

def setSavedFalse(key):
    global saved
    if(key.keysym.isalpha() or key.keysym.isdigit() or key.keysym in ["Return", "Tab", "Backspace", "Delete"]): #any key that changes text
        saved = False
        
def promptToSave():
       return messagebox.askyesnocancel("Save file?", "Do you want to save the current file?")

#initialization
app = Tk()
app.title("Writer")

#initializing text container
text = Text(app)

about = "A simple text editor in Python 3.5.2 using the Tkinter module for GUI programming. \nAuthor: Leo Hajder (leohajder.github.io)"

#menu
menubar = Menu(app)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "New", command = fNew)
filemenu.add_command(label = "Open", command = fOpen)
filemenu.add_command(label = "Save", command = fSave)
filemenu.add_command(label = "Save As", command = fSaveAs)
filemenu.add_separator()
filemenu.add_command(label = "About", command = lambda: messagebox.showinfo("About", about))
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = onExit)
menubar.add_cascade(label = "File", menu = filemenu)
app.config(menu=menubar)

#key Bindings
app.bind('<Control-n>', fNew)
app.bind('<Control-o>', fOpen)
app.bind('<Control-s>', fSave)
app.bind('<Key>', setSavedFalse)

#save before exit?
app.protocol("WM_DELETE_WINDOW", onExit)

#deploying text container
text.pack(expand=True, fill='both')

text.focus()

app.mainloop()
