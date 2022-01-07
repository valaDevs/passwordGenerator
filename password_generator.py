import random

# assets
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

pw_letters = int(input("How many letters would you like in your password ? \n"))
pw_numbers = int(input("How many numbers would you like in your password ? \n"))
pw_symbols = int(input("How many symbols would you like in your password ? \n"))

password_list = []

for char in range(1, pw_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, pw_numbers + 1):
    password_list.append(random.choice(numbers))
for char in range(1, pw_symbols + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
# convert to string
password = "" 
for i in password_list:
    password += i

print(f"Your password is ready ! ==> {password}")