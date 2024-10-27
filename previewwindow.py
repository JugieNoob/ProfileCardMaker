import tkinter as tk

def openPreview():
    global win
    win = tk.Tk(className=" Preview")
    win.geometry("320x240")
    win.resizable(False, False)
    
    img = tk.PhotoImage(file="image.png")
    
    preview = tk.Label(win)
    preview.pack()

    
    win.mainloop()

