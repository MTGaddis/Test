import random

def guess_the_number():
    difficulty_levels = {
        "easy": (1, 100),
        "medium": (1, 500),
        "hard": (1, 1000)
    }

    selected_difficulty = input("Select difficulty level (easy/medium/hard): ")
    selected_difficulty = selected_difficulty.lower()

    if selected_difficulty not in difficulty_levels:
        print("Invalid difficulty level. Defaulting to easy.")
        selected_difficulty = "easy"

    min_range, max_range = difficulty_levels[selected_difficulty]
    random_number = random.randint(min_range, max_range)
    attempts = 0

    while True:
        guess = int(input(f"Guess the number (between {min_range} and {max_range}): "))
        attempts += 1

        if guess == random_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < random_number:
            print("Too low! Guess a higher number.")
        else:
            print("Too high! Guess a lower number.")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        guess_the_number()
    else:
        print("Thank you for playing!")

guess_the_number()

