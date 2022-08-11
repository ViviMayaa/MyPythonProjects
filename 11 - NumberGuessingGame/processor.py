import random
print("""
 _______                           __                   _______                  __                    _______                        __ 
|     __|.--.--.-----.-----.-----.|__|.-----.-----.    |    |  |.--.--.--------.|  |--.-----.----.    |     __|.---.-.--------.-----.|  |
|    |  ||  |  |  -__|__ --|__ --||  ||     |  _  |    |       ||  |  |        ||  _  |  -__|   _|    |    |  ||  _  |        |  -__||__|
|_______||_____|_____|_____|_____||__||__|__|___  |    |__|____||_____|__|__|__||_____|_____|__|      |_______||___._|__|__|__|_____||__|
                                            |_____|                                                                                      
""")


def number_guessing_game():
    rounds = 0
    player_guess = 0
    print("I'm thinking of a number between 1 and 100.")
    difficulty_level = input("Please choose the difficulty. Type 'easy' or 'hard: ")
    secret_number_list = [i for i in range(1, 101)]
    secret_number = random.choice(secret_number_list)
    if difficulty_level == 'easy':
        rounds = 10
    elif difficulty_level == 'hard':
        rounds = 5
    else:
        print('Please type an available choice.')
        number_guessing_game()

    while rounds > 0:
        try:
            player_guess = int(input("Try a guess: "))
        except ValueError:
            print("Please type an available answer.")
            continue
        if player_guess == secret_number:
            print(f"Congrats, you have won! The number was {secret_number}\n")
            break
        elif player_guess > secret_number:
            print("Too high")
        elif player_guess < secret_number:
            print("Too low.")
        rounds -= 1
        print(f"Rounds remaining: {rounds}")
    if rounds == 0:
        print(f"You are out of attempts and the secret number was: {secret_number}\n")


number_guessing_game()
play_again = input("Want to try again? Y or N? ").upper()
if play_again == 'Y':
    number_guessing_game()
else:
    print('Thank you for playing! ')
    quit()

