import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '-', '_', '+', '=', '?']

print("Welcome to Python Password Generator!")
input_l = int(input("How many letters do you need in your passowrd?: "))
input_n = int(input("How many numbers do you need in your passowrd?: "))
input_s = int(input("How many symbols do you need in your password?: "))

password_list = []

for char in range(0, input_l):
  password_list.append(random.choice(letters))

for char in range(0, input_n):
  password_list.append(random.choice(numbers))

for char in range(0, input_s):
  password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
