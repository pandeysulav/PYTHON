# Inheritance = Allows a class to inherit attributes and methods from another class
# Helps with code reusability and extensibiility
#It is one of the most striking characteristics of OOP.
#       class Child(Parent)
#       Here Child is the subclass and Parent iss t

# class Animal:
#     def __init__ (self, name):
#         self.name = name
#         self.is_alive = True


#     def eat(self):
#         print(f"{self.name} is eating.")
    
#     def sleep(self):
#         print(f"{self.name} is asleep.")

# class Dog(Animal):
#     def speak(self):
#         print("WOOF!")

# class Cat(Animal):
#     def speak(self):
#         print("MEOW!")

# class Mouse(Animal):
#     def speak(self):
#         print("SQEEK!")

# dog = Dog("Scooby")
# cat = Cat("Garfield")
# mouse = Mouse("Mickey")

# print(dog.name)
# print(dog.is_alive)
# print(cat.name)
# print(cat.is_alive)
# cat.eat()
# dog.eat()
# dog.sleep()
# cat.speak()
# dog.speak()
# mouse.speak()

#MULTIPLE INHERITANCE: inherit from more than one parent class
#              C(A, B)

#MULTILEVEL INHERITANCE: inherit from a parent which inherits from another parent
#               C(B) <- B(A) <- A



# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def eat(self):
#         print(f"{self.name} is eating")
              
#     def sleep(self):
#         print(f"{self.name} is sleeping.")
              
# class Prey(Animal):
#     def flee(self):
#         print(f"{self.name} is fleeing.")

# class Predator(Animal):
#     def hunt(self):
#         print(f"{self.name} is hunting.")

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey, Predator):
#     pass

# rabbit = Rabbit("Bugs")
# hawk = Hawk("Tony")
# fish = Fish("Nemo")

# # rabbit.flee()
# # rabbit.eat()
# # hawk.hunt()
# # fish.flee()
# # fish.hunt()

# hawk.sleep()  
# rabbit.sleep()
# hawk.eat()
# hawk.hunt()
# fish.sleep()
# fish.hunt()



# super() = Function used in child class to call methods from a parent class(superclass).
# Allows you to extend the functionality of the inherited methods.


# class Shape:
#     def __init__(self, color, is_filled):
#         self.color = color
#         self.is_filled = is_filled
#     def describe(self):
#         print(f"It is {self.color} and {'filled.' if self.is_filled else 'not filled.'}")

# class Circle(Shape):
#     def __init__(self, color, is_filled, radius):
#         super().__init__(color, is_filled)
#         self.radius = radius

#     def describe(self):
#         super().describe()
#         print(f"It is a circle with an area of {3.14 * self.radius * self.radius} cm^2.")  # Method overwriting.

# class Square(Shape):
#     def __init__(self, color, is_filled, width):
#         super().__init__(color, is_filled)
#         self.width = width

#     def describe(self):
#         super().describe()
#         print(f"It is a square with an area of {self.width * self.width} cm^2.")  # Method overwriting.

# class Triangle(Shape):
#     def __init__(self, color, is_filled, width, height):
#         super().__init__(color, is_filled)
#         self.width = width
#         self.height = height
        
#     def describe(self):
#         super().describe()
#         print(f"It is a triangle with an area of {(self.width * self.height)/2} cm^2.")  # Method overwriting.

# circle = Circle(color="Red", is_filled = True, radius = 5)
# square = Square(color="Yellow", is_filled = True, width = 6)
# triangle = Triangle(color="Green", is_filled = False, width = 7, height=8)

# print(circle.color)
# print(circle.is_filled)
# print(circle.radius)


# print(square.color)
# print(square.is_filled)
# print(square.width)


# print(triangle.color)
# print(triangle.is_filled)
# print(f"Width: {triangle.width} cm")
# print(f"Height: {triangle.height} cm")

# circle.describe()
# square.describe()
# triangle.describe()


