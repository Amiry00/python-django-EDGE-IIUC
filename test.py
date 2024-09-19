import random

# Generate a random number between 1 and 100
correct_number = random.randint(1, 100)

# Allow the user up to 7 attempts to guess the number
attempts = 7

print("Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 100. You have 7 attempts.")

# Start the guessing game using a for loop
for attempt in range(1, attempts + 1):
    try:
        # Get the user's guess
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        # Check if the guess is out of range
        if guess < 1 or guess > 100:
            print("Invalid guess! Please enter a number between 1 and 100.")
            continue  # Skip the current attempt if the guess is out of range

        # Compare the guess with the correct number
        if guess < correct_number:
            print("Too low! Try again.")
        elif guess > correct_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the correct number {correct_number} in {attempt} attempts.")
            break  # Exit the loop if the user guesses the correct number
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# If the loop completes without a correct guess, show the correct number
else:
    print(f"Sorry, you've used all {attempts} attempts. The correct number was {correct_number}.")
