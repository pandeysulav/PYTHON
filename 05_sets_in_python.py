# # a = {1,3,5,6,7}
# # print(type(a))
# # print(a)

# # #Set is the collection of non-repetitive elements


# # #This syntax will create an empty dictionary and not an empty set
# # a = {}
# # print(type(a))

# # # An empty set can be created using the below syntax:
# b = set()
# # print(type(b))

# b.add(4)
# b.add(5)
# b.add((4,5,6)) # Cannot add list or dictionary to sets 
# # print(b)

# # b.add({4:5})
# print(len(b)) # Prints the lenght of this set

# b.remove(5) # Removes 5 from set b
# # b.remove(15) # Throws an error while trying to remove 15 (which is not in the set)
# print(b)
# print(b.pop())

# b.union()
# b.intersection()

# myDict = {
#     "pankha" : "Fan",
#     "Dabba" : "Box",
#     "Bastu" : "Item"
# }
# print("Options are", myDict.keys())
# a = input("Enter the Hindi word:\n")

# Below line will not throw an error if the word is not in the dictionary
# print("The meaning of your word is:", myDict.get[a])


# num1 = int(input("Enter number:\n"))
# num2 = int(input("Enter number:\n"))
# num3 = int(input("Enter number:\n"))
# num4 = int(input("Enter number:\n"))
# num5 = int(input("Enter number:\n"))
# num6 = int(input("Enter number:\n"))
# num7 = int(input("Enter number:\n"))
# num8 = int(input("Enter number:\n"))

# s = {num1, num2, num3, num4, num5, num6, num7, num8}
# print(s)

# s = {18, '18', 18.1}
# # Set prints unique value but data types don't really matter in sets
# print(s)

# s = set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(len(s))


# favLang = {}
# a = input ("Enter your favourite language Shubham \n")
# b = input ("Enter your favourite language Riwaz \n")
# c = input ("Enter your favourite language Sunil \n")
# d = input ("Enter your favourite language Ankit \n")
# favLang['Shubham'] = a
# favLang['Riwaz'] = b
# favLang['Sunil'] = c
# favLang['Ankit'] = d

# print(favLang)

