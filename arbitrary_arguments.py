# *args
# **kwargs


# def add(*nums):

#     total = 0
#     for num in nums:
#         total += num
#     return total

# print(add(1, 2, 3, 4,5, 6, 7, 8, 9, 10))  


# def display_names(*args):
#     """Display a list of names."""
#     for arg in args:
#         print(arg, end=" ")

# print(display_names("Alice", "Bob", "Charlie", "Diana", "Eve"))


#KWARGS

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# print_address(
#     street="123 Main St",
#     apt="Apt 4B",
#     city="Springfield",
#     state="IL",
#     zip_code="62701"
# )


# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()

#     if "apt" in kwargs:
#         print(kwargs.get("street"))
#         print(kwargs.get("apt"))
        
#     elif "pobox" in kwargs:
#         print(kwargs.get("street"))
#         print(kwargs.get("pobox"))

#     else:
#         print(kwargs.get("street"))
#         print(kwargs.get("city"))
#         print(kwargs.get("state"))
#         print(kwargs.get("zip_code"))
#         print(kwargs.get("country"))

# shipping_label(
#     "Dr.", "Spongebob", "Squarepants", "III",
#     street="123 Bikini Bottom",
#     pobox ="PO Box #1001",
#     city="Bikini Bottom",
#     state="Oceanic",
#     zip_code="12345",
#     country="Underwater"
# )
