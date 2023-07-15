import random
import csv

def guess_the_number():
    # Load high scores from a file
    high_scores = load_high_scores()

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
    max_attempts = 7  # Set the maximum number of attempts
    attempts = 0

    while attempts < max_attempts:
        guess = input(f"Guess the number (between {min_range} and {max_range}): ")

        # Validate user input
        if not guess.isdigit():
            print("Invalid input. Please enter a numeric value.")
            continue

        guess = int(guess)
        if guess < min_range or guess > max_range:
            print(f"Out of range. Please enter a number between {min_range} and {max_range}.")
            continue

        attempts += 1

        if guess == random_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")

            # Update high scores
            update_high_scores(selected_difficulty, attempts, high_scores)

            break
        elif guess < random_number:
            print("Too low! Guess a higher number.")
        else:
            print("Too high! Guess a lower number.")

        remaining_attempts = max_attempts - attempts
        print(f"You have {remaining_attempts} attempts remaining.")

    if attempts >= max_attempts:
        print("Game over! You have reached the maximum number of attempts.")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        guess_the_number()
    else:
        print("Thank you for playing!")

    # Save high scores to a file
    save_high_scores(high_scores)

def load_high_scores():
    try:
        with open("high_scores.csv", mode="r") as file:
            reader = csv.DictReader(file)
            high_scores = {row["Difficulty"]: int(row["Attempts"]) for row in reader}
    except FileNotFoundError:
        high_scores = {}
    return high_scores

def update_high_scores(difficulty, attempts, high_scores):
    if difficulty not in high_scores or attempts < high_scores[difficulty]:
        high_scores[difficulty] = attempts

def save_high_scores(high_scores):
    with open("high_scores.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Difficulty", "Attempts"])
        for difficulty, attempts in high_scores.items():
            writer.writerow([difficulty, attempts])

guess_the_number()
