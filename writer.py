from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

fileName = None
saved = True


def newFile(*args):
    global fileName, saved
    if not saved:
        save = promptToSave()
        if save:
            saveFile()
        elif save is None:
            return
    fileName = None
    text.delete(0.0, END)
    saved = True


def openFile(*args):
    global fileName, saved
    if not saved:
        save = promptToSave()
        if save:
            saveFile()
        elif save is None:
            return
    try:
        f = filedialog.askopenfile(
            filetypes=[('text files', '.txt'), ('all files', '.*')])
        if f:
            fileName = f.name
            t = f.read()
            text.delete(0.0, END)
            text.insert(END, t)
            saved = True
    except:
        messagebox.showerror("Error", "Unable to open file.")


def saveFile(*args):
    global fileName, saved
    t = text.get(0.0, END)
    if fileName:
        f = open(fileName, "w")
        f.write(t)
        f.close()
        saved = True
    else:
        saveFileAs()


def saveFileAs(*args):
    global saved
    f = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[
                                 ('text files', '.txt'), ('all files', '.*')])
    t = text.get(0.0, END)
    if f:
        try:
            f.write(t)
            f.close()
            saved = True
        except:
            messagebox.showwarning("Error", "Unable to save file.")


def onExit(*args):
    global saved
    if not saved:
        save = promptToSave()
        if save:
            saveFile()
        elif save is None:
            return
    app.destroy()


def setSavedFalse(key):
    global saved
    if (key.keysym.isalpha() or key.keysym.isdigit() or key.keysym in ["Return", "Tab", "Backspace",
                                                                       "Delete"]):  # any key that changes text
        saved = False


def promptToSave():
    return messagebox.askyesnocancel("Save file?", "Do you want to save the current file?")


# initialization
app = Tk()
app.title("Writer")

# initializing text container
text = Text(app)

about = "A simple text editor in Python 3.5.2 using the Tkinter module for GUI programming. \nAuthor: Leo Hajder (leohajder.github.io)"

# menu
menuBar = Menu(app)
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New", command=newFile)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="Save As", command=saveFileAs)
fileMenu.add_separator()
fileMenu.add_command(
    label="About", command=lambda: messagebox.showinfo("About", about))
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=onExit)
menuBar.add_cascade(label="File", menu=fileMenu)
app.config(menu=menuBar)

# key Bindings
app.bind('<Control-n>', newFile)
app.bind('<Control-o>', openFile)
app.bind('<Control-s>', saveFile)
app.bind('<Key>', setSavedFalse)

# save before exit?
app.protocol("WM_DELETE_WINDOW", onExit)

# deploying text container
text.pack(expand=True, fill='both')

text.focus()

app.mainloop()
