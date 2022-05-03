## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## deck of cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo
from replit import clear

def deal_card():
    """Returns a random card from the cards list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    
    return card

def calc_score(cards):
    """Takes a list of cards and returns the score calculated from the cards. Returns sum(cards)"""
    if sum(cards) == 21 and len(cards) == 2:
        return 21
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, comp_score):
    """Compares scores to determine the winner. Returns a win, lose, or draw statement."""
    
    if user_score > 21 and comp_score > 21:
        return "You went over. You lose 😤"
    
    if user_score == comp_score:
        return "Draw 🙃"
    elif comp_score == 21:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 21:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif comp_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > comp_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print(logo)
    print("Welcome to Blackjack! The computer is the dealer.\nYou can win by scoring 21 or by scoring higher than the dealer while not going over 21.")

    user_cards = []
    computer_cards = []
    game_over = False
    
    for num in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        #Used for when the player wants to keep drawing cards. 
        #Method: Create a bool and put into a while loop. The loop will run while the requirement is not meet 
        user_score = calc_score(user_cards)
        comp_score = calc_score(computer_cards)
        
        #Print statements will continue to update because they are in the loop
        print(f"\nYour Cards: {user_cards}, Curent Score: {user_score}")
        print(f"Computer's first card: [{computer_cards[0]}]")

        if user_score == 21 or comp_score == 21 or user_score > 21:
            game_over = True
        else:
            print("\nDo you want to draw another card?")
            draw_another_card = input("Type 'Y' for Yes. Type 'N' for No. ").lower()

            if draw_another_card == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True
    
    while comp_score != 21 and comp_score < 17:
        computer_cards.append(deal_card())
        comp_score = calc_score(computer_cards)
    
    print(f"\nYour Final Hand: {user_cards}, Final Score: {user_score}")
    print(f"Computer's Final Hand: {computer_cards}, Computer's Final score: {comp_score}")
    print(f"\n{compare(user_score, comp_score)}")

print(logo)
while input("\nWelcome to Blackjack! Do you want to play a game?\nType 'Y' for Yes. Type 'N' for No. ").lower() == 'y':
    clear()
    play_game()

