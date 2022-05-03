import random 
from replit import clear
from art import logo

def welcome_screen():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

def difficulty(choose_level):
    count = 0

    if choose_level == 'easy':
        count = 10
    elif choose_level == 'hard':
        count = 5
    
    return count

def validate_difficulty(choose_level):
    if choose_level == "easy" or choose_level == "hard":
        return "validated"
    else:
        return "Invalid option."

def pick_a_number():
    random_num = random.randint(1,100)
    return random_num

def compare_nums(user_guess, num_to_guess):
    if user_guess < 1 or user_guess > 100:
        print("Invalid number. Number not in range.")
    else:
        if user_guess < num_to_guess:
            print("Too low.")
        elif user_guess > num_to_guess:
            print("To high.")

def play_game():
    print(logo)
    choose_level = input("Great! Start by choosing a level of difficulty.\nType 'easy' or 'hard': ").lower()

    validate_level = validate_difficulty(choose_level)
    if validate_level == "validated":
        
        num_guesses = difficulty(choose_level)
        print(f"\nYou have {num_guesses} attempts to guess the number.")

        num_to_guess = pick_a_number()

        game_over = False
        while not game_over:
            user_guess = int(input("Make a guess: "))

            if user_guess == num_to_guess:
                print("\nGood job! You got it! 👍")
                print(f"The number was {num_to_guess}.")
                game_over = True
            else:  
                compare_nums(user_guess, num_to_guess)
            
                num_guesses -= 1
                if num_guesses == 0:
                    print("\nYou've run out of guesses. You lose! 👎")
                    print(f"The number was {num_to_guess}.")
                    game_over = True
                else:
                    print(f"\nGuess again. You have {num_guesses} remaining.")
    else:
        print("Invalid option.")

def play_again():
    print("\nDo you want to play again?")
    choice = input("Type 'Y' for Yes. Type 'N' for No: ").lower()
    if choice == 'n':
        print("\nThank you for playing!")
        return False
    else:
        return True

print(logo)
welcome_screen()
print("\nCan you guess the number?")

choice = input("Type 'Y' for Yes. Type 'N' for No: ").lower()
if choice == 'y':
    start_game = True
    while start_game:
        clear()
        play_game()
        start_game = play_again()
elif choice == 'n':
    print("\nYou can do it! Try again.")
    start_game = play_again()
    while start_game:
        clear()
        play_game()
        start_game = play_again()
else:
    print("Invalid option")
    

    







