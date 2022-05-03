#Functionalities 
    #display two entries with info from dictionary 
    #take in user input (choice of entry)
    #compare to two entries 
    #keep track of rounds won (current score)
    #reset A and B after each round won
    #Lose: End game. Display final score.
    #Ask if the player wants to play again
    #display logo and versus art

from game_data import data
import random
from art import logo
from replit import clear

def select_comparisons():
    comparisons = {}
    for entry in range(2):
        comparisons[entry] = random.choice(data)
    return comparisons

def print_comparisons(options):
    compare_a = options[0]
    compare_b = options[1]
    
    if compare_a:
        print(f"Compare A: {compare_a['name']}, a {compare_a['description']} from {compare_a['country']}.")
        print(f"DELETE LATER: {compare_a['follower_count']}")
        
    if compare_b:
        print(f"\nAgainst B: {compare_b['name']}, a {compare_b['description']} from {compare_b['country']}.")
        print(f"DELETE LATER: {compare_b['follower_count']}")

def compare_followers(options):
    compare_a = options[0]
    num_followers_a = compare_a['follower_count']
    
    against_b = options[1]
    num_followers_b = against_b['follower_count']
    
    if num_followers_a > num_followers_b:
        return 'a'
    elif num_followers_b > num_followers_a:
        return 'b'

def play_again():
    print("Do you want to play again?")
    choice = input("Type 'Y' for Yes. Type 'N' for No. ").lower()
    
    if choice == 'y':
        return 'y'
    else:
        return 'n'

def game():
    game_over = False
    count = 0

    while not game_over:
        options = select_comparisons()
        print_comparisons(options)

        print("\nWho has more Instagram followers?")
        user_selection = input("Type 'A' or 'B': ").lower()

        if user_selection == 'a' or user_selection == 'b':
            higher_followers = compare_followers(options)

            if user_selection == higher_followers:
                clear()
                print(logo)
                count += 1
                print(f"You're right! Current score: {count}\n")
            else:
                clear()
                print(logo)
                print(f"Sorry. Wrong guess. Final score: {count}\n")
                game_over = True

                Yes_No = play_again()
                if Yes_No == 'y':
                    game_over = False
                    count = 0
                    clear()
                    print(logo)
                else:
                    print("\nThank you for playing.")
        else: 
            print("fix later")
            print("\nInvalid option!")
            game_over = True

            Yes_No = play_again()
            if Yes_No == 'y':
                game_over = False
                count = 0
                clear()
                print(logo)
            else:
                print("\nThank you for playing.")

print(logo)
game()


    



