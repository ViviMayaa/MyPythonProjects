
print("""
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
""")
print("Welcomed to the secret auction! You bit, others bit, but we only know the result after it ends! Good luck!")
play_again = 'yes'
dict_of_bitters = {}
higher_bid = 0
higher_bitter = {}
while play_again == 'yes':
    name = input("Please type the name of the bitter: \n")
    price = int(input("Please input the price you will be betting: "))
    dict_of_bitters[name] = price
    print(dict_of_bitters)
    play_again = input("Want to add more bitters? Yes or no?\n").strip().lower()

    for elements in dict_of_bitters:
        if dict_of_bitters[elements] > higher_bid:
            higher_bitter.clear()
            higher_bid = dict_of_bitters[elements]
            higher_bitter[elements] = dict_of_bitters[elements]
higher_bitter = [element for element in higher_bitter.keys()]

print(f"And the winner is {higher_bitter[0].title()} with a bet of ${higher_bid}!")


