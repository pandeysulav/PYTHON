import random
import time

def spin_row():
    symbols = ["🍒", "🍋", "🍉", "🔔", "⭐"]
    
    # 65% chance to return a winning row (3 matching symbols)
    if random.random() < 0.75:
        symbol = random.choice(symbols)
        return [symbol, symbol, symbol]
    
    # 35% chance to return a non-winning random row
    while True:
        row = [random.choice(symbols) for _ in range(3)]
        if not (row[0] == row[1] == row[2]):
            return row


def print_row(row):
    print("\n" + "*" * 40)
    print("  |  ".join(row))
    print("\n" + "*" * 40)

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    return 0

def main():
    balance = 1000

    print("\n" + "*" * 40)
    print("Welcome to the Python Slot Machine Program!")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("\n" + "*" * 40)

    while balance > 0:
        print(f"Your current balance is: ${balance:.2f}")
        bet = input("Place your bet amount: $").strip()

        if not bet.isdigit():
            print("Invalid bet amount. Please enter a valid number.")
            continue

        bet = int(bet)
        if bet > balance:
            print("Insufficient balance for this bet. Please try again.")
            continue

        if bet <= 0:
            print("Bet amount must be positive. Please try again.")
            continue

        balance -= bet

        print("Spinning", end="", flush=True)
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print()

        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"Congratulations! You won ${payout:.2f}!")
        else:
            print("Sorry, you didn't win this time.")

        balance += payout

        if balance <= 0:
            print("You have run out of money! Game over.")
            break

        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            break

    print(f"Game over! Your final balance is: ${balance:.2f}")

if __name__ == "__main__":
    main()
