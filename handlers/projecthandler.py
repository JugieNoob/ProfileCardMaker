import json
import os

id = 1

jsonformat = {
    "w": 500,
    "h": 400,
    "bgcolor": [255, 255, 255],

    "elements": {}
}

def newProject(projname=f"untitled-{id}"):
    global id
    id = id + 1
    os.mkdir(f"temp/{projname}")
    file = open(f"temp/{projname}/main.json", "x")
    file.write(json.dumps(jsonformat, indent=4))