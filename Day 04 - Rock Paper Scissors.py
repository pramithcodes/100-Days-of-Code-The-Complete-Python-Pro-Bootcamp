import random

rock = '''
_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

print("Welcome to Rock Paper and Scissors Game!")
user_choice = int(input("What would you choose? 0 - Rock, 1 - Paper, and 2 - Scissors: "))
if user_choice >=0 and user_choice <=2:
    print(game_images[user_choice])
computer_choice = random.randint(0, 2)
print("Computer chose: ")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You have typed a wrong number, try again!")
elif user_choice == 0 and computer_choice == 2:
    print("Yay! You win.")
elif computer_choice == 0 and user_choice == 2:
    print("Oops! You lose.")
elif computer_choice > user_choice:
    print("Oops! You lose.")
elif computer_choice < user_choice:
    print("Yay! You win.")
elif computer_choice == user_choice:
    print("It's a draw, you are lucky!")
