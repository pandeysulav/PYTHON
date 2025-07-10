
# # Use open function to read the content of your file

# f = open('sample.txt', 'r') # By default, the mode is r
# data = f.read(5) # reads first 5 characters from the file
# # data = f.read()
# print(data)
# f.close()


# f = open('sample.txt', 'r')
# # read first line
# data = f.readline()
# print(data)
# # read second line
# data = f.readline()
# print(data)
# # read third line
# data = f.readline()
# print(data)
# f.close()

# f = open("another.txt", 'a')
# f.write('I am appending ')
# f.close()

# WITH STATEMENTS
# with open("another.txt", 'w') as f:
#     a = f.write()
# print(a)

# f = open('poems.txt')
# t = f.read()
# if 'twinkle'.lower() in t:
#     print('Twinkle is present')
# else:
#     print('Twinkle is not present')
# f.close()

# game function
# def game():
#     return 70

# score = game()
# with open("hiscore.txt") as f:
#     hiscore = f.read()
    
# if hiscore == '':
#    with open("hiscore.txt", "w") as f:
#         f.write(str(score))


# elif int(hiscore)<score :
#     with open("hiscore.txt", "w") as f:
#         f.write(str(score))

# with open("sample.txt") as f:
#     content = f.read()

# content = content.replace("donkey", "######")

# with open("sample.txt", "w") as f:
#     f.write(content)

# content = True
# i = 1
# with open("logfile.txt") as f:
#     while content:

#         content = f.readline()
    
#         if 'python' in content.lower():
#             print(content)
#             print(f"Yes, python in present in the file on line number {i}.")
#         i+=1
#     # else:
#     #     print("No, python is not present")

# with open ("this.txt") as f:
#     content = f.read()

# with open("copy.txt", "w") as f:
#     f.write(content)

file1 = "this.txt"
file2 = "copy.txt"

with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()

if f1==f2:
    print("The two files are identical.")
else:
    print("The two files are not identical.")
