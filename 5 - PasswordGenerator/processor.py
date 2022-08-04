import random
import string
print("Welcome to the PyPassword Generator!\n")
password = ''

amount_of_letters = int(input("How many letters would you like in your password?\n"))
amount_of_symbols = int(input("How many symbols would you like?\n"))
amount_of_numbers = int(input("How many numbers would you like?\n"))

while amount_of_letters != 0 or amount_of_numbers != 0 or amount_of_symbols != 0:
    random_number = random.randint(0, 2)
    if random_number == 0 and amount_of_letters != 0:
        password += string.ascii_letters[random.randint(0, 51)]
        amount_of_letters -= 1
    elif random_number == 1 and amount_of_numbers != 0:
        password += str(random.randint(0, 10))
        amount_of_numbers -= 1
    elif random_number == 2 and amount_of_symbols != 0:
        password += str(string.punctuation[random.randint(0, 31)])
        amount_of_symbols -= 1

#  would work if same quantity:
# random = ''.join([random.choice(string.ascii_letters + string.digits  ) for n in range(12)])
print(f"Here is your password: {password}")