import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '-', '_', '+', '=', '?']

print("Welcome to Python Password Generator")
input_l = int(input("How many letters do you want in your password?: "))
input_n = int(input("How many numbers do you want in your passwod?: "))
input_s = int(input("How many numbers do you want in your password?: "))

password = ""

for char in range(1, input_l + 1):
  password += random.choice(letters)

for char in range(1, input_n + 1):
  password += random.choice(numbers)

for char in range(1, input_s + 1):
  password += random.choice(symbols)

print(password)
