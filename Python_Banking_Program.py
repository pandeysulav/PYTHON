def show_balance(balance):
    print("\n" + "*" * 40)
    print(f"*{'Your current balance is: $' + format(balance, '.2f'):^38}*")
    print("*" * 40 + "\n")    

def deposit():
    print("\n" + "*" * 40)
    amount = float(input("Enter the amount to deposit: $"))
    print("*" * 40 + "\n")
    
    if amount < 0:
        print("*" * 40)
        print(f"*{'Deposit amount must be positive.':^38}*")
        print("*" * 40 + "\n")
        return 0
    else:
        print(f"*{'You have successfully deposited $' + format(amount, '.2f'):^38}*")
        print("*" * 40 + "\n")
        return amount

def withdraw(balance):
    print("\n" + "*" * 40)
    amount = float(input("Enter the amount to withdraw: $"))
    print("*" * 40 + "\n")
    
    if amount > balance:
        print("*" * 40)
        print(f"*{'Insufficient funds for this withdrawal.':^38}*")
        print("*" * 40 + "\n")
        return 0
    elif amount < 0:
        print("*" * 40)
        print(f"*{'Withdrawal amount must be positive.':^38}*")
        print("*" * 40 + "\n")
        return 0
    else:
        print(f"*{'You have successfully withdrawn $' + format(amount, '.2f'):^38}*")
        print("*" * 40 + "\n")
        return amount

def print_menu():
    print("\n" + "*" * 40)
    print(f"*{'Welcome to the Banking Program!':^38}*")
    print("*" * 40)
    print(f"*{'1. Show Balance':<38}*")
    print(f"*{'2. Deposit':<38}*")
    print(f"*{'3. Withdraw':<38}*")
    print(f"*{'4. Exit':<38}*")
    print("*" * 40 + "\n")

def main():
    balance = 0
    is_running = True

    print_menu()

    while is_running:
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)

        elif choice == '2':
            balance += deposit()

        elif choice == '3':
            balance -= withdraw(balance)

        elif choice == '4':
            is_running = False

        else:
            print("\n" + "*" * 40)
            print(f"*{'That is not a valid choice. Please try again.':^38}*")
            print("*" * 40 + "\n")

        if is_running:
            print_menu()

    print("\n" + "*" * 40)
    print(f"*{'Thank you for using the Banking Program. Goodbye!':^38}*")
    print("*" * 40 + "\n")

if __name__ == "__main__":
    main()
