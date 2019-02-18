class Color:
    """A class to define RGB colors"""
    def __init__(self, name, red, green, blue):
        # instance variables unique to each instance
        self.name = name
        self.red = red
        self.green = green
        self.blue = blue
        
blue = Color("boring blue", 0, 0, 255)
green = Color("normal green", 0, 255, 0)
# print(isinstance(a, str))
print(blue.name)
