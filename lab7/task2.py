from PIL import Image

source1 = Image.open("boiWings.png")
source2 = Image.open("boiAngel.png")
source3 = Image.open("boiSkull.png")

#source1.show()


s1b = source1.width
s1a = source1.height

s2a = source2.width
s2b = source2.height

s3a = source3.width
s3b = source3.height

dimensionW=s1b+s2a+s3a+50
dimensionH=s1a+s2b+s3b+50

im = Image.new("RGB", (dimensionW,dimensionH), "grey")

def imposeImage(source,width):
    x1=width
    for x in range(source.width):
        y1=0
        for y in range(source.height):
            color1 = source.getpixel((x,y))
            #print(color1)
            im.putpixel((x1,y1),color1)
            y1+=1
        x1+=1


imposeImage(source1,0)
imposeImage(source2,s1b+10)
imposeImage(source3,s2a+s1b+20)

#source1.show()
im.save("newEmpty.png")
im.show()

