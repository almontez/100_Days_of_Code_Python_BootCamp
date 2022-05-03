from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction!\n")

bids = {}

add_bids = True

while add_bids:
    name = input("Name: ")
    amount = float(input("Bid: $"))

    bids[name] = amount

    print("\nAre there other bids?")
    more_bids = input("Type 'yes' or 'no': ").lower()

    if more_bids == "no":
        add_bids = False
    
    clear()

top_bid = 0
for key in bids:
    if bids[key] > top_bid:
        top_bid = bids[key]
        name_top_bid = key

print(f"The winner is {name_top_bid} with a bid of ${top_bid}. Congratulations!")
