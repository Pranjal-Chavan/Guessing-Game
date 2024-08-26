import random

def guessing_game():
    random_number = random.randint(1, 100)
    
    attempts = 0
    correct_guess = False
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    
    while not correct_guess:
        try: 
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number correctly.")
                correct_guess = True
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Display the number of attempts it took
    print(f"It took you {attempts} attempts to guess the number.")

# Run the game
guessing_game()
