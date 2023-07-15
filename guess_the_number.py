import random

def guess_the_number():
    random_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess the number (between 1 and 100): "))
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
