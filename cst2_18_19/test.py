class MyClass:
    """ A simple class"""
    i = 44444
    def __init__(self, str):
        self.my_string=str
        
    def hello(self):
        print("helo")
        return 'hello world'
    
    def give_string(self):
        print(self.my_string)

x = MyClass("Schoool")
print(x.i)
print(MyClass.__doc__)
print(MyClass.i)
print(x.hello())
print(x.my_string)
x.give_string
