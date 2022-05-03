from game_data import data
from art import logo
from replit import clear
import random


def select_comparisons():
    return random.choice(data)

def format_data(comparisons):
    name = comparisons['name']
    descriptions = comparisons['description']
    country = comparisons['country']

    return f"{name}, a {descriptions} from {country}."

def answer(user_selection, comparison_a, comparison_b):
    num_followers_a = comparison_a['follower_count']
    num_followers_b = comparison_b['follower_count']

    if num_followers_a > num_followers_b:
        correct_guess = 'a'
    elif num_followers_b > num_followers_a:
        correct_guess = 'b'
    
    if user_selection == correct_guess:
        return True
    else: 
        return False

def play_again():
    print("\nDo you want to play again?")
    choice = input("Type 'Y' for Yes. Type 'N' for No. ").lower()
    
    if choice == 'y':
        return 'y'
    else:
        print("\nThank you for playing! To play again, restart game.")
        return 'n'

def game():
    print(logo)
    count = 0 
    game_over = False

    while not game_over:
        comparison_a = select_comparisons()
        comparison_b = select_comparisons()

        while comparison_a == comparison_b:
            comparison_b = select_comparisons

        print(f"Compare A: {format_data(comparison_a)}\n")
        print(f"Against B: {format_data(comparison_b)}")

        print("\nWho has more Instagram followers?")
        user_selection = input("Type 'A' or 'B': ").lower() 
        
        if user_selection == 'a' or user_selection == 'b':
            guess = answer(user_selection, comparison_a, comparison_b)

            clear()
            print(logo)
            if guess == True: 
                count += 1
                print(f"You're right! Current Score: {count}.\n")
            else:
                print(f"Sorry. Wrong guess. Final score: {count}.")
                game_over = True
        else:
            print("Invalid Option")
            game_over = True

            
game()
while play_again() == 'y':
    clear()
    game()

        

