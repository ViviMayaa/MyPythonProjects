from story_reader import story_reader
from images import lake, treasure, door, hole, fish, fire, beast, lost

story_reader = story_reader()
tentativa = True


def reader(line_number):
    for element in story_reader[line_number]:
        print(element, end="")


while tentativa == True:
    tentativa= False
    reader(line_number=0)
    reader(line_number=1)
    reader(line_number=2)
    choice = input('\n').strip().lower()
    if choice == 'right':
        hole()
        reader(line_number=3)
        try_again = input("Try again? Yes or no?\n").strip().lower()
        if try_again == "yes":
            tentativa = True
            continue
        break
    elif choice == "left":
        lake()
        reader(line_number=4)
        choice = input('\n').strip().lower()
        if choice == 'swim':
            fish()
            reader(line_number=5)
            try_again = input("Try again? Yes or no?\n").strip().lower()
            if try_again == "yes":
                tentativa = True
                continue
            break
        elif choice == 'wait':
            door()
            reader(line_number=6)
            choice = input('\n').strip().lower()
            if choice == 'red':
                fire()
                reader(line_number=7)
                try_again = input("Try again? Yes or no?\n").strip().lower()
                if try_again == "yes":
                    tentativa = True
                    continue
                break
            if choice == 'blue':
                beast()
                reader(line_number=8)
                try_again = input("Try again? Yes or no?")
                try_again = input("Try again? Yes or no?\n").strip().lower()
                if try_again == "yes":
                    tentativa = True
                    continue
                break
            if choice == 'yellow':
                treasure()
                reader(line_number=9)
                quit()
            else:
                lost()
                reader(line_number=10)
                try_again = input("Try again? Yes or no?\n").strip().lower()
                if try_again == "yes":
                    tentativa = True
                    continue
                break
    else:
        print("You typed wrong, try again!\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        tentativa = True


print("The End.")

