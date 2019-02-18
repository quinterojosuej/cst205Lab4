from PIL import Image
source1 = Image.open("EmiliePreyer.jpg")

print("Size of " + str(source1.width) + " by " + str(source1.height))
#print(source1.getpixel((100,100)))
def tammyShop():
    for x in range(source1.width):
        for y in range(source1.height):
            temmmie = source1.getpixel((x,y))
            if(temmmie[0] == 255):
                return temmmie

print(tammyShop())
