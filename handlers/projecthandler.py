import json
import os
import handlers.imagehandler as imagehandler
import tkinter.filedialog as fd
import zipfile

id = 1


jsonformat = {
    "w": 500,
    "h": 400,
    "bgcolor": [255, 255, 255],

    "elements": {}
}

def newProject(newprojname=f"untitled-{id}"):
    global projname
    global id
    id = id + 1
    projname = newprojname
    print(projname)
    os.mkdir(f"temp/{newprojname}")
    os.mkdir(f"temp/{newprojname}/assets")
    file = open(f"temp/{newprojname}/main.json", "x")
    file.write(json.dumps(jsonformat, indent=4))
    
    

def loadProject():
    projinfo = fd.askopenfile(filetypes=[("Project Files", "*.pcmp"), ("All Files", "*")])
    projname = os.path.basename(projinfo.name).replace(".pcmp", "")


    with zipfile.ZipFile(projinfo.name, "r") as projdir:
        projdir.extractall(f"temp/{projname}")
      
    imagehandler.loadProject(projname)
    

def saveProject():
    print(f"Hello {projname}")
    proj = zipfile.ZipFile(f"{projname}.pcmp", "w", zipfile.ZIP_DEFLATED)
    for item in os.listdir(f"temp/{projname}"):
        proj.write(item, f"temp/{projname}")