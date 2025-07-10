import random
from words_list import words 

hangman_art = {
    0: ("  ",
        "  ",
        "  "),
    1: (" o ",
        "  ",
        "  "),
    2: (" o ",
        " | ",
        "  "),
    3: (" o ",
        "/|",
        "  "),
    4: (" o ",
        "/|\\",
        "  "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")
}

def display_hangman(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    # Display the hint as a continuous string (spaces stay visible)
    print("\nWord to guess: " + "".join(hint) + "\n")

def display_answer(answer):
    print("Word: " + "".join(answer).upper())  # No spaces between letters

def print_separator():
    print("\n" + "-" * 40 + "\n")

def main():
    print("=" * 40)
    print("    WELCOME TO THE HANGMAN GAME!    ")
    print("=" * 40)

    answer = random.choice(words).lower()

    # Initialize hint: spaces are shown, letters hidden as '_'
    hint = [c if c == ' ' else '_' for c in answer]

    wrong_guesses = 0
    guessed_letters = set()

    while True:
        display_hangman(wrong_guesses)
        display_hint(hint)

        guess = input("Guess a letter: ").lower()

        print_separator()

        if len(guess) != 1 or not guess.isalpha():
            print("❗ Please enter a single valid letter (a-z).")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            print("✅ Good guess!")
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            print(f"❌ Wrong guess! You have {6 - wrong_guesses} tries left.")

        print("Letters guessed:", ", ".join(sorted(guessed_letters)))

        if "_" not in hint:
            print_separator()
            print("🎉 Congratulations! You guessed the word:")
            display_answer(answer)
            print("=" * 40)
            break

        if wrong_guesses >= 6:
            display_hangman(wrong_guesses)
            print_separator()
            print("💀 Game Over! The correct word was:")
            print(answer.upper())
            print("=" * 40)
            break

if __name__ == "__main__":
    main()
