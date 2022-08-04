print("Welcome to the Tip Calculator!")

try:
    bill = float(input("Please type the total bill: \n"))
    amount_of_people = int(input("How many people to split the bill? \n"))
    tip = float(input("What percentage tip would you like to give? \n"))

except ValueError:
    print("Value most be a number.")
    raise ValueError
result = (bill + (bill * (tip/100))) / amount_of_people

print(f"Each person should pay: ${round(result, 2)}")
#or with 00
result = "{:.2f}".format(result)
print(f"Each person should pay: ${result}")