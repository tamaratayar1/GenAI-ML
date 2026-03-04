import random

print("Welcome to the Guessing Game!")

while True:

    secret_number = random.randint(1, 100)

    for attempt in range(7):

        guess = int(input("Guess a number between 1 and 100: "))

        if guess < secret_number:
            print("Too Low!")
        elif guess > secret_number:
            print("Too high!")
        else: 
            print(f"You guessed the number! It was {secret_number}.")
            break

        print(f"You have {6 - attempt} guesses left")

    else:
        print(f"You didn't guess the number :( It was {secret_number}.")

    play_again = input("Want to play again? Type Yes or No: "). strip().lower()

    if play_again not in ("yes", "y", "yep"):
        print("Thanks for playing!")
        break
