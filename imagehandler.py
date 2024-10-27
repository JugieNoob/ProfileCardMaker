from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import json

w = 500
h = 350

image = Image.new("RGB", (w, h), (255, 255, 255)) # Standard size 1920x1080


def addElement(type, x = 0, y = 0, color = [0, 0, 0], textproperties = ["Your Text Here", "Corbel", 32], imagedir = "OIG2.jpg", bannerheight = 50):
    draw = ImageDraw.Draw(image)
    if (textproperties[1] != None and textproperties[2] != None):
        font = ImageFont.truetype(f'fonts/{textproperties[1]}.ttf', textproperties[2])
    if (imagedir != None):
        newimg = Image.open(imagedir)
   
    print(w)
    match type: 
        case "banner":
            draw.rectangle((x, y, w, bannerheight), fill=(color[0], color[1], color[2]))
        case "text": 
            draw.text((x, y), text=textproperties[0], fill=(color[0], color[1], color[2]), font=font)
        case "bannerwithtext":
            draw.rectangle((x, y, w, 50), fill=(color[0], color[1], color[2]))
            draw.text((25, 15), text=textproperties[0], fill=(color[0], color[1], color[2]), font=font)
        case "image":
            image.paste(newimg, (x, y))
        case "bulletpoints":
            for i in range(0, len(textproperties[0])):
                draw.text((x, y + ((50 + textproperties[2] + ((textproperties[0][i - 1].count("\n") + 1) * 25)) * i)), text="• " + textproperties[0][i], fill=(color[0], color[1], color[2]), font=font)
    pass

def loadProject():
    with open("axolotl.json") as file:
        
        global image
        global w
        global h
        
        data = json.load(file)
        
        w = data["w"]
        h = data["h"]
        bgcolor = data["bgcolor"]
       
        image = Image.new("RGB", (w, h), (bgcolor[0], bgcolor[1], bgcolor[2]))
        
        for i in data["elements"]:
            element = data["elements"][i]
            
            if "color" not in element:
                element["color"] = None
            if "font" not in element:
                element["font"] = None
            if "text" not in element:
                element["text"] = None
            if "size" not in element:
                element["size"] = None
            if "imagedir" not in element:
                element["imagedir"] = None
            if "bannerheight" not in element:
                element["bannerheight"] = None

                
            addElement(i, element["x"], element["y"], element["color"], [element["text"], element["font"], element["size"]], element["imagedir"], element["bannerheight"])


loadProject()

image.save("image.png")
print("new image")