import magichue
from mss import mss
from PIL import Image

def find_dominant_color(filename):
    #Resizing parameters
    width, height = 150,150
    image = Image.open(filename)
    image = image.resize((width, height),resample = 0)
    #Get colors from image object
    pixels = image.getcolors(width * height)
    #Sort them by count number(first element of tuple)
    sorted_pixels = sorted(pixels, key=lambda t: t[0])
    #Get the most frequent color
    dominant_color = sorted_pixels[-1][1]
    return dominant_color

light = magichue.Light('192.168.1.4')
image_path = 'monitor-1.png'

while(True):
    with mss() as sct:
        sct.shot()
        light.rgb = find_dominant_color(image_path)
