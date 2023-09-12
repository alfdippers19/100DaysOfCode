import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for x in range(0, nr_letters):
    rnd = random.randint(0,len(letters)-1)
    password.append(letters[rnd])
for x in range(0, nr_symbols):
    rnd = random.randint(0,len(symbols)-1)
    password.append(symbols[rnd])
for x in range(0, nr_numbers):
    rnd = random.randint(0,len(numbers)-1)
    password.append(numbers[rnd])

for x in range(0, len(password)):
    temp = password[x]
    rnd = random.randint(0,len(password)-1)
    password[x] = password[rnd]
    password[rnd] = temp

password_str = ""
for char in password:
    password_str += char

print(password_str)