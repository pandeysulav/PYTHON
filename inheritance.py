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



class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
              
    def sleep(self):
        print(f"{self.name} is sleeping.")
              
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing.")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting.")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

# rabbit.flee()
# rabbit.eat()
# hawk.hunt()
# fish.flee()
# fish.hunt()

hawk.sleep()  
rabbit.sleep()
hawk.eat()
hawk.hunt()
fish.sleep()
fish.hunt()
