"""
Created by Jonathan Quintero and Jesus Gomez
For cst205 hw4
~~~~~~The Following code will create a website in which 
random images will be displayed as choices and the user
can click on an image to receive more information regarding 
athe image. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
#The following modules are needed for flask, random numbers and image usage
from flask import Flask, render_template
from random import randint
from PIL import Image
#The following will allow for flask to run with its appropiate name and modules
app=Flask(__name__)
#The following is the data taht is provided for the images and used for more details 
#in the second more details site. Stored as an array of dictionaries.
image_info = [
             {
                 "id" : "34694102243_3370955cf9_z",
                 "title" : "Eastern",
                 "flickr_user" : "Sean Davis",
                 "tags" : ["Los Angeles", "California", "building"]
                 },
             {
                 "id" : "37198655640_b64940bd52_z",
                 "title" : "Spreetunnel",
                 "flickr_user" : "Jens-Olaf Walter",
                 "tags" : ["Berlin", "Germany", "tunnel", "ceiling"]
                 },
             {
                 "id" : "36909037971_884bd535b1_z",
                 "title" : "East Side Gallery",
                 "flickr_user" : "Pieter van der Velden",
                 "tags" : ["Berlin", "wall", "mosaic", "sky", "clouds"]
                 },
             {
                 "id" : "36604481574_c9f5817172_z",
                 "title" : "Lombardia, september 2017",
                 "flickr_user" : "Mónica Pinheiro",
                 "tags" : ["Italy", "Lombardia", "alley", "building", "wall"]
                 },
             {
                 "id" : "36885467710_124f3d1e5d_z",
                 "title" : "Palazzo Madama",
                 "flickr_user" : "Kevin Kimtis",
                 "tags" : [ "Rome", "Italy", "window", "road", "building"]
                 },
             {
                 "id" : "37246779151_f26641d17f_z",
                 "title" : "Rijksmuseum library",
                 "flickr_user" : "John Keogh",
                 "tags" : ["Amsterdam", "Netherlands", "book", "library", "museum"]
                 },
             {
                 "id" : "36523127054_763afc5ed0_z",
                 "title" : "Canoeing in Amsterdam",
                 "flickr_user" : "bdodane",
                 "tags" : ["Amsterdam", "Netherlands", "canal", "boat"]
                 },
             {
                 "id" : "35889114281_85553fed76_z",
                 "title" : "Quiet at dawn, Cabo San Lucas",
                 "flickr_user" : "Erin Johnson",
                 "tags" : ["Mexico", "Cabo", "beach", "cactus", "sunrise"]
                 },
             {
                 "id" : "34944112220_de5c2684e7_z",
                 "title" : "View from our rental",
                 "flickr_user" : "Doug Finney",
                 "tags" : ["Mexico", "ocean", "beach", "palm"]
                 },
             {
                     "id" : "36140096743_df8ef41874_z",
                     "title" : "Someday",
                     "flickr_user" : "Thomas Hawk",
                     "tags" : ["Los Angeles", "Hollywood", "California", "Volkswagen", "Beatle", "car"]
                     }
             ]
#The following creates a random number appropiate to the deatailed data available.
def randomizer():
    x = randint(0,8)
    return x
#The following is where the options site is created, path of /
@app.route('/')
def home():
    #The following three lines ensure that no repeats occur between the options
    a,b,c = randomizer(), randomizer(), randomizer()
    while(a==b or a==c or b==c):
        a,b = randomizer(), randomizer()
    #The following lines call the global details data and gives the random values
    first_pic = image_info[a]
    second_pic = image_info[b]
    third_pic = image_info[c]
    #The following return commands the rendering of flask.html, or our options 
    #site with the dictionaries that were randomly picked
    return render_template('flask.html',first_pic=first_pic,second_pic=second_pic,third_pic=third_pic)
#The following is where the more detailed view is created, path /picture/<id>
@app.route('/picture/<id>')
#Our site requires that the last site's image is shown, so its id is a parameter
def t_test(id):
    #var is created to be referenced later
    var = 0
    #In the for loop we obtain the id of the image chosen from the previous site
    #and cycle through our image_info to find its corresponding dictionary.
    for i in range(len(image_info)):
        if(image_info[i]['id']==id):
            var=image_info[i]
    #We then open the image to obtain the values not on the dictionary
    img = Image.open('static/images/'+id+'.jpg')
    mode = img.mode
    form = img.format
    width, height = img.size
    #The following return renders our more detailed site, secondFlask.html with the 
    #data it will display
    return render_template('secondFlask.html',id=id,var=var,mode=mode,form=form,width=width,height=height)
#The follwoing allows for the file to itself in flask, as the line in line 14
if __name__=='__main__':
    app.run(debug=True)


