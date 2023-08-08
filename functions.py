from PIL import Image, PngImagePlugin
from os.path import join
from os import listdir, mkdir

class Img(PngImagePlugin.PngImageFile):
    pass

def getImage(location:str,name:str) -> Img:
    img = Image.open(join(location,name))
    return img

def checkImage(img:Img) -> list[bool,str]:
    print(type(img))
    h,w = img.size 
    if h != w:
        return False, "\nImage MUST have the same width and height!"
    if h%256 + w%256 != 0:
        return False, "\nImage size MUST be some multiple of 256!"
    return True, "\nImage correct proportion and size, cutting begins now..."

def cut(zoom_lvl:int, img:Img, max_zoom:int):
    tiles = []
    nr_of_tiles = 2**zoom_lvl
    w, h = img.size
    d = w/nr_of_tiles

    for i in range(0,nr_of_tiles):
        x_layer = []
        for j in range(0,nr_of_tiles):
            box = (i*d, j*d, i*d+d, j*d+d)
            x_layer.append(img.crop(box))
        tiles.append(x_layer)


    for i,x_set in enumerate(tiles):
        mkdir(join("map_tiles",str(zoom_lvl),str(i)))
        for j,y_img in enumerate(x_set):
            w,h = y_img.size
            if w*zoom_lvl/max_zoom > 256:
                y_img = y_img.resize((int(w*zoom_lvl/max_zoom/2),int(h*zoom_lvl/max_zoom/2)))
            y_img.save(join("map_tiles",str(zoom_lvl),str(i),str(j)+".png"),"png")
    return

def runProgram(max_zoom:int):
    source_img_name = listdir("image_to_cut")
    print(f'\nSource image found with the name {source_img_name[0]}')
    source_img = getImage("image_to_cut",source_img_name[0])
    cont, message = checkImage(source_img)
    print(message)
    if cont:
        zoom_level = 0
        mkdir(join("map_tiles",str(zoom_level)))
        mkdir(join("map_tiles",str(zoom_level),"0"))
        w,h = source_img.size
        to_save = source_img.resize((int(w/max_zoom),int(h/max_zoom)))
        to_save.save(join("map_tiles","0","0","0.png"),"png")
        zoom_level += 1
        while zoom_level <= max_zoom:
            mkdir(join("map_tiles",str(zoom_level)))
            print(f'\nCutting zoom level {zoom_level}...')
            cut(zoom_level,source_img,max_zoom)
            zoom_level += 1
        print("\nFinished! Find your tiles in the map_tiless folder!")
