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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Python Treasure Island!")
print("Your mission is to find the treasure. Choose the right path to reach it safely. Wishing you the best of luck on your journey!")

choice_1 = input("You are at a crossroad, where do yo want to go? Left or Right: ")
if choice_1 == "Left":
    choice_2 = input("You have came to a seashore and there is a island in the middle of the sea. Type Boat and wait or Type Swim across the sea: ")
    if choice_2 == "Boat":
        choice_3 = input("You have arrived the island safely. There is a home with 3 doors infront of you, which one will you choose? Red, Yellow or Green: ")
        if choice_3 == "Red":
            print("Yay! You win the treasure.")
        else:
            print("You entered the wrong door. GAME OVER.\nTRY AGAIN.")
    else:
        print("Oops! You got attacked by the Shark. GAME OVER.\nTRY AGAIN")
else:
    print("Oops! You fell into a well, GAME OVER.\nTRY AGAIN")
