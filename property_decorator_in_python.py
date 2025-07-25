# @property = Decorator used to define a method as a property (it can be accessed like an attri
#         Benefit: Add additional logic when read, write, or delete attributes
#         Gives you getter, setter and deleter method

class Rectangle:
    def _init_(self, width, height):
        self.width = width
        self.height = height

