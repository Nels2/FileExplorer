# Tkinter file explorer by Nels2


from tkinter import *
from tkinter import filedialog

def browseFiles():
    # browser window
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))

    # change label contents
    label_file_explorer.configure(text="File Opened: "+filename)


# creates the root window
window = Tk()
# set window title
window.title('File Explorer')
# set window size
window.geometry("500x500")
# set background color of window
window.config(background = "white")
# create a file exp. label
label_file_explorer = Label(window,
        text = "File Explorer using Tkinter",
        width = 100, height = 4,
        fg = "blue")

button_explore = Button(window,
        text = "Browse Files",
        command = browseFiles)

button_exit = Button(window,
        text = "Exit",
        command = exit)

# grid method is chosen for placing the widgets in a table structure by specfiying rows/columns.
label_file_explorer.grid(column = 1, row = 1)
button_explore.grid(column = 1, row = 2)
button_exit.grid(column = 1, row = 3)

#let window wait for events, if any
window.mainloop()
