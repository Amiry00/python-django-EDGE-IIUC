#Home task-2:Guess the number game
#importing the random module
import random
#generating a random number between 1 and 100
secret_number = random.randint(1,100)
print("Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 100. You have 7 attempts.")
#allowing the user up to 7 attempts to guess the number
for attempt in range(7):
    #taking the user's guess
    guess = int(input(f"Attempt {attempt+1}:")) 
    #checking if the guess is out of range
    if guess < 1 or guess > 100:
            print("Invalid guess! Please enter a number between 1 and 100.")   
    if guess < secret_number:
        print("Your guess is below the number, please guess again")
    elif guess > secret_number:
              print("Your guess is above the number, please guess again")  
    else:     
      print(f"Congratulations! You've guessed the correct number {secret_number} in {attempt+1} attempts.")
      break
#If the loop completes without a correct guess, show the correct number
if guess != secret_number:
  print(f"Nope,The correct number is   {secret_number}")