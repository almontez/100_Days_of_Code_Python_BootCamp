print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n") 

print("After wandering around Treasure Island for a few days, you notice a single road diverging left and right.\n")
choice1 = input("Which side do you choose? ").lower()
if choice1 == "left":
  print("\nGood choice! It's always better to go left than right!")
  print("Your choice has led you to the bank of a large and sprawling river.\n")
  
  choice2 = input("Do you want to swim or wait? ").lower()
  if choice2 == "wait":
    print("\nGood instincts! If you had tried to swim the hungry anaconda, lying in wait, may have eaten you.")
    print("Instead, your patience is rewarded. A boat, with snake-savvy, river sailing monkeys, comes your way.")
    print("They stop and offer you a ride across the river. You accept.")
    print("The monkeys tell you that just up ahead is a magical cave. \nLegend tells that that is where the treasure is hidden. BE WARNED: DANGER ALSO AWAITS.\n")
    
    choice3 = input("Do you proceed? Yes or No? ").lower()
    if choice3 == "yes":
      print("\nTreasure awaits for those who are brave! You continue walking and make it to the cave. You come upon 3 doors. Behind two doors lies death. Behind one treasure.\n")

      choice4 = input("Which door do you choose? Blue, Yellow, or Red? ").lower()
      if choice4 == "yellow":
        print("\nI knew you would make it! Good choice. Yellow like the color of gold. You're rich! You've struck gold!")
      elif choice4 == "blue" or choice4 == "red":
        print("\nYou were one door away from gold. But, you choose wrong so now it's GAME OVER. You fall into a hole with spikes at the bottom. YOU'RE DEAD!")
      else:
        print("Invalid Choice.")
    elif choice3 == "no":
      print("\nFortune favors the bold. You are smitted by lightening for your cowardly choice.") 
    else: 
      print("Invalid Choice.")
  elif choice2 == "swim":
    print("\nOh! No! You should have waited. In your impatience, you didn't notice the anaconda waiting for you to cross. It swallows you whole, digesting you slowly over the course of 5 days.") 
  else:
    print("Invalid Choice.")
elif choice1 == "right":
  print("\nWrong choice. Right's isn't always right. This path has led you to a field filled with zombies. You are eaten alive.")
else:
  print("Invalid Choice.")