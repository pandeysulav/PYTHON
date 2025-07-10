import random


print("Welcome to the Dice Roller Program!\n")

# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐",
"│         │",
"│    ●    │",
"│         │",
"└─────────┘"

dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: (
        "┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"), 
    3: (
        "┌─────────┐",      
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: (
        "┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: (
        "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",      
        "└─────────┘"),
    6: (
        "┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"
    )
}

dice = []
total = 0
num_of_dice = int(input("How many dice would you like to roll? \n"))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

for die in dice:
    for line in dice_art.get(die):  
        print(line)

for die in dice:
    total += die
print(f"Total sum obtained is: {total}")

print("Thank you for using the Dice Roller Program!")
