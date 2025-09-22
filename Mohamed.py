print("hello World")
import random

def int_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            val = int(input(prompt))
            if min_val is not None and val < min_val:
                print(f"Enter a number >= {min_val}")
                continue
            if max_val is not None and val > max_val:
                print(f"Enter a number <= {max_val}")
                continue
            return val
        except ValueError:
            print("Please enter a valid integer.")

def choose_difficulty():
    print("\nSelect difficulty:")
    print("1) Easy   — range 1-100, 10 attempts")
    print("2) Medium — range 1-500, 8 attempts")
    print("3) Hard   — range 1-1000, 6 attempts")
    print("4) Custom")
    choice = int_input("Choose 1-4: ", 1, 4)
    if choice == 1:
        return 1, 100, 10
    if choice == 2:
        return 1, 500, 8
    if choice == 3:
        return 1, 1000, 6
    # custom
    low = 1
    high = int_input("Enter max number (>=10): ", 10)
    attempts = int_input("Enter max attempts (>=1): ", 1)
    return low, high, attempts

def play_game():
    low, high, max_attempts = choose_difficulty()
    secret_number = random.randint(low, high)
    attempts = 0

    print(f"\nGuess the number between {low} and {high}. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        guess = int_input(f"Attempt {attempts+1}/{max_attempts} - Enter your guess: ", low, high)
        attempts += 1

        if guess < secret_number:
            print("⬆️ The number is higher")
        elif guess > secret_number:
            print("⬇️ The number is lower")
        else:
            print(f"🎉 Congratulations! You guessed the number in {attempts} attempts")
            return

    print(f"❌ Out of attempts. The number was {secret_number}.")

def main():
    print("👋 Welcome to the Number Guessing Game!")
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()