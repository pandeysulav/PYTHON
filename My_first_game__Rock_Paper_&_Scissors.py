import random  
#Rock Paper Scissors or Snake Water Gun

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True
    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True

print("Comp turn: Rock(r), Paper(p) or Scissors(s)?")
randNo = random.randint(1,3)

# print(randNo) # Commented for code clarity
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("Your turn: Rock(r), Paper(p) or Scissors(s)?\n").lower()

while you not in ['r', 's' , 'p']:
    print("Invalid input! Please choose Rock(r), Paper(p) or Scissors(s)")
    you = input("Your turn: Rock(r), Paper(p) or Scissors(s)?\n")

a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a == True:
    print("You Win!")
else:
    print("You Lose!")


