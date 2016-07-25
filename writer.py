from tkinter import *

filename = None

def fNew():
    global filename
    t = text.get(0.0, END)
    filename = "Untitled"
    text.delete(0.0, END)

def fOpen():
    global filename
    try:
        f = filedialog.askopenfile(filetypes = [('text files', '.txt'),('all files', '.*')])
        filename = f.name
        t = f.read()
        fileContent = t
        text.delete(0.0, END)
        text.insert(END, t)
    except:
        messagebox.showwarning("Error", "Unable to open file.")
           
def fSave():
    global filename
    t = text.get(0.0, END)
    if(filename):
        f = open(filename, "w")
        f.write(t)
        f.close()
    else:
        fSaveAs()

def fSaveAs():
    f = filedialog.asksaveasfile(filetypes = [('text files', '.txt'),('all files', '.*')])
    t = text.get(0.0, END)
    try:
        f.write(t)
        f.close()
    except:
        messagebox.showwarning("Error", "Unable to save file.")

writer = Tk()
writer.title("Writer")

text = Text(writer)

#menu
menubar = Menu(writer)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "New", command = fNew)
filemenu.add_command(label = "Open", command = fOpen)
filemenu.add_command(label = "Save", command = fSave)
filemenu.add_command(label = "Save As", command =fSaveAs)
filemenu.add_separator()
filemenu.add_command(label = "About", command = lambda: messagebox.showwarning("About", "A simple text editor made for fun and practice with Python 3.5.2 using the Tkinter module for GUI programming. \nAuthor: Leo Hajder (github.com/lhajder)"))
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = writer.destroy)
menubar.add_cascade(label = "File", menu = filemenu)
writer.config(menu=menubar)

text.pack(expand=True, fill='both')

text.focus()

writer.mainloop()
