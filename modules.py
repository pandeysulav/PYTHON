# help("modules")


# import math as m

# print(m.pi)
# print(m.sqrt(16))
# print(m.factorial(5))
# print(m.pow(2, 3))
# print(m.exp(2))

pi = 3.14159

def square(x):
    return x**2

def cube(x):
    return x**3

def circumference(radius):
    return 2 * pi * radius

def area(radius):
    return pi * square(radius)

result1 = pi
result2 = square(5)
result3 = cube(3)

print("Value of pi:", result1)
print("Square of 5:", result2)
print("Cube of 3:", result3)

