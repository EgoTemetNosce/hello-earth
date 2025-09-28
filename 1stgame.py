import random

def guess_the_number():
    print("🎮 Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 20...")

    secret_number = random.randint(1, 20)
    attempts = 0

    while True:
        guess = input("Take a guess: ")
        
        # Make sure the player typed a number
        if not guess.isdigit():
            print("Please enter a valid number!")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Woooooo Correct! The number was {secret_number}.")
            print(f"You guessed it in {attempts} tries.")
            break

if __name__ == "__main__":
    guess_the_number()
