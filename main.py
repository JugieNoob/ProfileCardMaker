import tkinter as tk
import handlers.imagehandler as imagehandler
import handlers.projecthandler as projecthandler

import previewwindow
import atexit



win = tk.Tk(className=" Title Card Maker")
win.geometry("640x480")
win.resizable(False, False)

#previewwindow.openPreview()

# Adding a menubar
menu = tk.Menu(win)
fileMenu = tk.Menu(menu, tearoff=False)
fileMenu.add_command(label="New Project", accelerator="Ctrl + N", command=projecthandler.newProject)
fileMenu.add_command(label="Save Project", accelerator="Ctrl + S", command=print)
fileMenu.add_command(label="Open Project", accelerator="Ctrl + O", command=print)
fileMenu.add_separator()
fileMenu.add_command(label="Export Image", accelerator="Ctrl + E", command=imagehandler.exportImage)


helpMenu = tk.Menu(menu, tearoff=False)
helpMenu.add_command(label="Info", accelerator="F1", command=print)

menu.add_cascade(menu=fileMenu, label="File")
menu.add_cascade(menu=helpMenu, label="Help")
    

def onExit():
    #Write a function to remove every file from temp folder
    pass

atexit.register(onExit)


win.config(menu=menu)
win.mainloop()