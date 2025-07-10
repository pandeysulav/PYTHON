# def percent(marks):
#     return ((marks[0] + marks[1] + marks[2] + marks[3] + marks[4])/400)*100
    
# marks1 = [45, 78, 86, 77, 86]
# percentage1 = percent(marks1)

# marks2 = [75, 98, 56, 47, 56]
# percentage2 =  percent(marks2)
# print(percentage1,percentage2)


# def greet(name):
#     print("Good Day, " + name)

# greet("Sulav")


# def mySum(num):
#    return sum(num)       # Returns the sum of the list passed as 'num'

# num1 = [1,2,3,4,5,6,7]   # First list
# sum1 = mySum(num1)       # Calls mySum with num1

# num2 = [5,7,8,9,12,23]   # Second list
# sum2 = mySum(num2)       # Calls mySum with num2

# print(sum1, sum2)        # Prints the two sums


# Recursions in python

# n! = 1 * 2 * 3 * 4 * 5 .... n
# n! = [1 * 2 * 3 * 4 * 5 .... n-1] * n
# n! = (n-1)! * n
# n = 7
# product = 1
# for i in range(n):
#     product = product * (i+1)
# print(product)


# def factorial_iter(n):
#     product = 1
#     for i in range(n):
#         product = product * (i+1)
#     return(product)

# def factorial_recursive(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * factorial_recursive(n-1)


# f = factorial_iter(5)
# f = factorial_recursive(7)
# print(f)

# def max(num1, num2, num3):
#     if (num1>num2):
#         if(num1>num3):
#             return num1
#         else:
#             return num3
#     elif (num2>num1):
#         if(num2>num3):
#             return num2
#         else:
#             return num3   
#     else:
#         return num3 

# m = max(3, 5, 6)
# print("The value of the maximum number is: " + str(m))

# def farh(cel):
#     return (cel * (9/5)) + 32

# c = 0
# f = farh(c)
# print("The Fahrenheit temperature is: " + str(f))

# print("Hello,", end = " ")
# print("How", end = " ")
# print("are", end = " ")
# print("you?", end = " ")

# def sum_recursive(n):
#     if n == 0:
#         return 0
#     return  n + sum_recursive(n-1)

# # f = factorial_iter(5)
# f = sum_recursive(5)
# print(f)

# n = 7
# for i in range(n):
#     print("*" * (n-i)) #Prints * n-i times

# def cem(inches):
#     return inches*2.54

# i = 5
# print(cem(i))

# def remove_and_split(string, word):
#     newStr = string.replace(word, "")
#     return newStr.strip()

# this = "   Harry is a good    "
# n = remove_and_split(this, "Harry")
# print(n)

# def mult(num):
#     for i in range(1,11):
#         print(f"{num} x {i} = {num * i}")
    
# mult(5)


# a = 5
# b = 3
# print(f"The sum of {a} and {b} is {a + b}.")


# Function to wish someone a happy birthday


# def happy_birthday(name, age):
#     print(f"Happy Birthday to you, {name}!")
#     print(f"You are {age} years old today, {name}!")
#     print("Wishing you all the best on your special day!\n")

# happy_birthday("Alice", 30)
# happy_birthday("Bob", 25)
# happy_birthday("Charlie", 22)

# def add(x,y):
#     return x + y

# print(f"The value of the sum of the two numbers is: {add(5, 3)}") 


# def sum(a,b):
#     w = a + b
#     return w

# def sub(a,b):
#     x = a - b
#     return x

# def mult(a,b):  
#     y = a * b
#     return y

# def div(a,b):
#     if b == 0:
#         return "Division by zero is not allowed."
#     z = a / b
#     return z

# print(sum(10, 5))  # Output: 15
# print(sub(10, 5))  # Output: 5  
# print(mult(10, 5))  # Output: 50
# print(div(10, 5))  # Output: 2.0


# def create_name(first_name, last_name):
#     first = first_name.capitalize()
#     last = last_name.capitalize()
#     return (f"Your name is: {first} {last}")

# print(create_name("sulav", "pandey"))