import random

def get_random_number():
    return random.randint(1, 100)

def evaluate_guess(guess, correct_number):
    if guess < correct_number:
        return "Higher!"
    elif guess > correct_number:
        return "Lower!"
    else:
        return "Congratulations! You guessed the number!"

def play_game():
    correct_number = get_random_number()
    attempts = 0
    max_attempts = 10
    
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")
    
    while attempts < max_attempts:
        try:
            guess = int(input("What is your guess? "))
            attempts += 1
            result = evaluate_guess(guess, correct_number)
            print(result)
            
            if guess == correct_number:
                print(f"You guessed it in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number!")
    
    if attempts == max_attempts:
        print(f"Sorry! You've used all your attempts. The correct number was {correct_number}.")

if __name__ == "__main__":
    play_game()
