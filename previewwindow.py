import tkinter as tk
from PIL import Image

def openPreview():
    global win
    win = tk.Tk(className=" Preview")
  #  win.geometry(f"")
    win.resizable(False, False)
    
    img = Image.open("image.png")#.resize((int(img.size[0] / 4), int(img.size[1] / 4)))
    win.geometry(f"{int(img.size[0] / 4)}x{int(img.size[1] / 4)}")

    imgl = tk.PhotoImage(img)
    print(img)
    
    preview = tk.Label(image=imgl)
    preview.pack()

    win.mainloop()

