# Description
# Implement a Rectangle class which include the following 
# attributes and methods:

# Two public attributes width and height.
# A constructor which expects two parameters width and height of type int.
# A method getArea whichi would calculate 

class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def getArea(self) -> int:
        return self.width * self.height
