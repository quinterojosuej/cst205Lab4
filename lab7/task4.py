from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
#import math
from PIL import Image

def distance(color_1, color_2):
    rgb_one = (color_1[0],color_1[1],color_1[2])
    #print(rgb_one) 
    rgb_two = (color_2[0],color_2[1],color_2[2])
    # start with the two rgb tuples
    #rgb_one = (255, 255, 255)
    #rgb_two = (0, 0, 0)

    # next you have to initialize sRGBColor objects from your tuples
    s_rgb_one = sRGBColor(rgb_one[0], rgb_one[1], rgb_one[2])
    s_rgb_two = sRGBColor(rgb_two[0], rgb_two[1], rgb_two[2])

    # next you convert the sRGBColor object to a LabColor
    lab_rgb_one = convert_color(s_rgb_one, LabColor)
    lab_rgb_two = convert_color(s_rgb_two, LabColor)

    # now you can calculate the distance of the two LabColors using the delta_e function
    """
    print("The distance between white and black is", delta_e_cie2000(lab_rgb_one, lab_rgb_two))
    print("The distance between black and black is", delta_e_cie2000(lab_rgb_two, lab_rgb_two))
    """

    fore = delta_e_cie2000(lab_rgb_one, lab_rgb_two)
    #print(fore)
    return fore

def chromakey(source, bg):
    for x in range(source.width):
        for y in range(source.height):
            cur_pixel = source.getpixel((x,y))
            green = (0, 190, 60)
            if distance(cur_pixel, green) < 10:
                # grab the color at the same spot from the new background
                source.putpixel((x,y), bg.getpixel((x,y)))
    source.save("chroma1.png")
    
    
weather = Image.open("boiBossess.jpg")
fruit = Image.open("green.jpg")
chromakey(weather, fruit)
