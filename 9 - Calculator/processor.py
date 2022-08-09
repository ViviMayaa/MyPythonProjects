from math_functions import MathFunctions
import image
image.calculator_typed()
image.calculator_image()
play_again = True


while play_again:
    def input_numbers():
        try:
            first_number = float(input("Type the first number: "))
            second_number = float(input("Type the second number: "))
            return first_number, second_number
        except ValueError:
            print("Invalid input, please type again.")
            input_numbers()

    numbers = input_numbers()
    first_number = numbers[0]
    second_number = numbers[1]
    operation_dict = {
        "+": MathFunctions.addition(first_number, second_number),
        "-": MathFunctions.subtraction(first_number, second_number),
        "*": MathFunctions.multiplication(first_number, second_number),
        "/": MathFunctions.division(first_number, second_number)
    }

    def format_float(number):
        return "{:.2f}".format(number)

    def calc():

        operation = input("Please chose the operation type: + - * / ")
        try:
            print(f"The {operation} between {first_number} and {second_number} is: "
                  f"{format_float(operation_dict[operation])}")
        except KeyError:
            print("Invalid input, please type again.")
            calc()

        # if operation == '+':
        #     print(MathFunctions.addition(first_number, second_number))
        # elif operation == '-':
        #     print(MathFunctions.subtraction(first_number, second_number))
        # elif operation == '*':
        #     print(MathFunctions.multiplication(first_number, second_number))
        # elif operation == '/':
        #     print(MathFunctions.division(first_number,second_number))
        #
        # else:
        #     print("Invalid input, please type again.")
        #     calc()

    calc()
    answer_play_again = input("Want to calculate again? Y or N ? ").upper()
    play_again = True if answer_play_again == 'Y' or answer_play_again == "YES" else False

print("Thank you for using! ")
