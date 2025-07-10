# def day_of_week(day):
#     if day == 0:
#         return "Sunday"
#     elif day == 1:
#         return "Monday"
#     elif day == 2:
#         return "Tuesday"
#     elif day == 3:
#         return "Wednesday"
#     elif day == 4:
#         return "Thursday"
#     elif day == 5:
#         return "Friday"
#     elif day == 6:
#         return "Saturday"
#     else:
#         return "Not a valid day hacker boy."
    
#Match-case statement is the alternative to if-elif-else statement in Python 3.10 and above.
# a = day_of_week(10)
# print(a)


# def day_of_week(day):
#     match day:
#         case 0:
#             return "Sunday"
#         case 1:
#             return "Monday"
#         case 2:
#             return "Tuesday"
#         case 3:
#             return "Wednesday"
#         case 4:
#             return "Thursday"
#         case 5:
#             return "Friday"
#         case 6:
#             return "Saturday"
#         case _:
#             return "Not a valid day hacker boy."

# print(day_of_week("pizza")) 


# def is_weekend(day):
#     match day:
#         case "Sunday":
#             return True
#         case "Saturday":
#             return True
#         case "Monday":
#             return True
#         case "Tuesday":
#             return False
#         case "Wednesday":
#             return False
#         case "Thursday":
#             return False
#         case "Friday":
#             return False



# print(is_weekend("Saturday"))

#The alternative method to do this is given below:

# def is_weekend(day):
#     match day:
#         case "Sunday"|"Saturday":
#             return True
#         case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
#             return False
#         case _:
#             return "Not a valid day"
    

# print(is_weekend("Saturday"))





