#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letter= int(input("How many letters would you like in your password?\n"))
symbol = int(input(f"How many symbols would you like?\n"))
number = int(input(f"How many numbers would you like?\n"))


password = []
for x in range(1,letter +1):
    password += random.choice(letters)

for x in range(1,symbol +1):
    password += random.choice(symbols)

for x in range(1,number +1):
    password += random.choice(numbers)

print(password)

random.shuffle(password)

newPass = ""

for y in password:
    newPass += y

print(newPass)





