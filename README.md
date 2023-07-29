# CysTileCutter
I made this tile-cutter program to use together with my CysMaps! I made this becasue I was unhappy with other tile-cutting programs : )

## What is tile-cutting?
Tile-cutting is used by Google Maps and Leaflet, this allows you to zoom in on maps while retaining the quality of the image and speed of the website.

Usually, this include some downscaling of the quality when you zoom out, and increase when you zoom in. To ensure that your viewers only see what they need to, and not a pixel more.

## Zoom level
Zoom level is how far you wish to be able to zoom into your image. think of it as how many time we cut your image up in perfectly square areas. Zoom level 0 is your whole image, with 0 cuts, while zoom level 1 is your whole image cut once horizontally and once vertically.

To figure out how many tiles you will get for a given zoom level, use the following formula:
$$ n = 2^z $$
Where $n$ is the number of tiles and $z$ is the desired zoom level.

To get the correct size for your maximum zoom level, ensure that your full image has the size PxP, where P is defined as:
$$ P = 256 * 2^z $$
and z is defined as your maximum zoom level.

## How to use this program
- Copy this repository by downloading it from [here](https://github.com/Cyandied/CysTileCutter) or using solutions like GitKraken
- Delete all .gitkeep files!
- Use ```pip install -r req.txt``` to install all dependencies
- Place your map in the ***image_to_cut*** folder
    - Image prerequisites and tips:
        - Image height and width must be the same
        - Image height and width must be some multiple of 256
        - Image should be of the highest quality possible
- Define your zoom level by changing the number in the function ```runProgram(x)```, the default is 4
- Run the program with ```python program.py```
- Find your tiles in the ***result*** folder!

## Why can I not use any size image I want?
I am making this to work easily with [Leaflet](https://leafletjs.com/), and I enjoy using common conventions.

So:
- Perfectly square map ensures that coordinated work without issues in [Leaflet](https://leafletjs.com/)
- Convention for other tile-cutting programs is that the smallest tile is 256x256 pixels