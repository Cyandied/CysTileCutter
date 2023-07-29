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

def cut(zoom_lvl:int):
    tiles = []
    for x_coord in listdir(join("result",str(zoom_lvl-1))):
        right = []
        left = []
        for y_coord in listdir(join("result",str(zoom_lvl-1),x_coord)):
            img = Image.open(join("result",str(zoom_lvl-1),x_coord,y_coord))
            this_right, this_left = crop(img)
            for i in range(0,2):
                right.append(this_right[i])
                left.append(this_left[i])
        tiles.append(right)
        tiles.append(left)
    for i,x_set in enumerate(tiles):
        mkdir(join("result",str(zoom_lvl),str(i)))
        for j,y_img in enumerate(x_set):
            y_img.save(join("result",str(zoom_lvl),str(i),str(j)+".png"),"png")
    return

def crop(img:Img) -> list[list[Img,Img],list[Img,Img]]:
    h,w = img.size

    ur = img.crop((0,0,w/2,h/2))
    ul = img.crop((w/2,0,w,h/2))

    lr = img.crop((0,h/2,w/2,h))
    ll = img.crop((w/2,h/2,w,h))
    return [ur,lr],[ul,ll]

def runProgram(max_zoom:int):
    source_img_name = listdir("image_to_cut")
    print(f'\nSource image found with the name {source_img_name[0]}')
    source_img = getImage("image_to_cut",source_img_name[0])
    cont, message = checkImage(source_img)
    print(message)
    if cont:
        zoom_level = 0
        mkdir(join("result",str(zoom_level)))
        mkdir(join("result",str(zoom_level),"0"))
        source_img.save(join("result","0","0","0.png"),"png")
        zoom_level += 1
        while zoom_level <= max_zoom:
            mkdir(join("result",str(zoom_level)))
            print(f'\nCutting zoom level {zoom_level}...')
            cut(zoom_level)
            zoom_level += 1
        print("\nFinished! Find your tiles in the results folder!")
