number = 4

number_list = [2, 3, 4, 5, 6, 7, 8, 9]
if number % number == 0 and number % 1 == 0:
    for element_number_list in number_list:
        if number % element_number_list == 0 and element_number_list != number:
            print("It's not a prime number.")
            quit()

    print("It's a prime number.")
else:
    print("It's not a prime number.")