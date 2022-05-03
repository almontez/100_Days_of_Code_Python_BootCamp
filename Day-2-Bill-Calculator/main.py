print("Welcome to the bill calculator!\n")

total_bill = float(input("What was the total bill? $"))
tip_percent = float(input("What percentage tip would you like to give? 10, 12, 15...? "))
num_ppl = int(input("How many people will split the bill? "))

bill_with_tip = ((tip_percent / 100) * total_bill) + total_bill
bill_per_person = bill_with_tip / num_ppl
formatted_amount = "{:.2f}".format(bill_per_person)

print(f"\nEach person should pay: ${formatted_amount}")

