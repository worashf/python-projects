import random

def guess_number(upper_bound):
    random_number = random.randint(1, upper_bound)
    attempts = 0

    while True:
        try:
            user_guess = int(input(f"Enter your guess: "))
            if not 1 <= user_guess <= upper_bound:
                raise ValueError(f"Please enter a number between 1 and {upper_bound}")
        except ValueError as e:
            print(f"Invalid input: {e}")
            continue

        attempts += 1

        if user_guess == random_number:
            print(f"Congratulations! You guessed correctly within {attempts} attempts.")
            break
        elif random_number < user_guess:
            print("Too high! Try guessing lower.")
        else:
            print("Too low! Try guessing higher.")

# Input validation for the upper guess range
while True:
    try:
        guess_range = int(input("Enter the upper guess range: "))
        if guess_range < 1:
            raise ValueError("Please enter a positive number.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}")

guess_number(guess_range)