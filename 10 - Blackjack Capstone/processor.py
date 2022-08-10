from time import sleep
from useful import positive_feedback, cards
import random
from art import ArtModels


class BlackjackGame:
    player_hand = []
    total_player = 0
    player_points = 0
    rounds = 6
    computer_hand = []
    total_computer = 0
    computer_points = 0

    @classmethod
    def start_blackjack(cls):
        answer_play = input("Would you "
                            "like to hear an "
                            "explanation on the game? \n")
        if positive_feedback(answer_play=answer_play):
            tutorial()
        cls.processor()

    @classmethod
    def processor(cls):
        player_bust = False
        computer_bust = False
        print("Let's Play!!\n")
        ArtModels.many_cards()
        while cls.rounds > 0:
            print(f"Rounds remaining : {cls.rounds}")
            answer_play = input("Would you like to get a new card? \n")
            if positive_feedback(answer_play=answer_play):
                cls.player_hand = new_card()
                print(f"You got the card: "
                      f"{cls.player_hand['card_type']} "
                      f"{cls.player_hand['card_art']}")
                if cls.player_hand["card_type"] == 'Ace Card':
                    ace_value = ace_player_treatment()
                    cls.total_player += ace_value
                else:
                    cls.total_player += cls.player_hand['card_value']
                if cls.total_player > 21:
                    print("Your total is more than 21, is a bust! ! You lose!")
                    player_bust = True
                    break
            else:
                pass

            if computer_choice(cls.total_computer):
                cls.computer_hand = new_card()
                print(f"Computer got the card: "
                      f"{cls.computer_hand['card_type']} "
                      f"{cls.computer_hand['card_art']}")
                if cls.computer_hand["card_type"] == 'Ace Card':
                    ace_value = ace_computer_treatment(cls.total_computer)
                    cls.total_computer += ace_value
                else:
                    cls.total_computer += cls.computer_hand["card_value"]
                if cls.total_computer > 21:
                    print("Computer total is more "
                          "than 21, is a bust! You win!")
                    computer_bust = True
                    break
            else:
                print("Computer has passed.")
                pass
            cls.rounds -= 1
            print(f"Player {cls.total_player}"
                  f" x {cls.total_computer} Computer\n")

        if player_bust:
            print("Computer has won!\n")
            cls.computer_points += 1
        elif computer_bust:
            print("Player has won! \n")
            cls.player_points += 1
        elif cls.total_player > cls.total_computer:
            print("Player has won! \n")
            cls.player_points += 1
        elif cls.total_player < cls.total_computer:
            print("Computer has won!\n")
            cls.computer_points += 1
        elif cls.total_computer == cls.total_player:
            print("Is a Draw! \n")

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
              "Points~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"                      Player "
              f"{cls.player_points} X {cls.computer_points} Computer ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        cls.play_again()

    @classmethod
    def play_again(cls):
        play_again = True
        while play_again:
            play_again = input("Would you like play again? \n")
            if positive_feedback(answer_play=play_again):
                cls.player_hand.clear()
                cls.total_player = 0
                cls.rounds = 6
                cls.computer_hand.clear()
                cls.total_computer = 0
                cls.processor()
            else:
                print("Thank you for playing! See you next time! \n")
                ArtModels.symbols()
                quit()


def computer_choice(total_computer):
    # Giving the computer a more human way of thinking,
    # lowering the chances of getting a card the closer it gets to 21
    if total_computer < 10:
        return True

    elif total_computer < 17:
        choice = random.randint(0, 1)
        if choice == 0:
            return True
        else:
            return False

    elif total_computer < 19:
        choice = random.randint(0, 2)
        if choice == 0:
            return True
        else:
            return False
    elif total_computer < 21:
        choice = random.randint(0, 10)
        if choice == 0:
            return True
        else:
            return False
    else:
        return False


def new_card():
    player_hand = random.choice(cards())
    return player_hand


def ace_computer_treatment(total_computer):
    if total_computer < 10:
        return 11
    else:
        return 1


def ace_player_treatment():
    try:
        ace_value = \
            int(input("Please choose between 1 "
                      "and 11 as value to give to your Ace Card: \n"))
        if ace_value == 11 or ace_value == 1:
            return ace_value
        else:
            print("Invalid input, please chose a value of 1 or 11.")
            ace_player_treatment()

    except ValueError:
        print("Invalid input, please chose a value a number between 1 or 11.")
        ace_player_treatment()


def tutorial():
    sleep(1)
    print("\nBlackjack, or 21, is a"
          " game where both parties take cards out of a"
          " deck as much as they want and,"
          " at the end, the one closer to the 21 number wins!\n")
    sleep(2)
    print("If one passes the 21 mark when adding all"
          " cards numbers, however, they are automatically"
          " disqualified!\n")
    sleep(2)
    print("You will have a total of 6 rounds to play"
          " against the computer, however don't expect your"
          " adversary to be predictable as a machine would!\n")
    sleep(2)
    print("Attention, however, that if you get a"
          " Ace Card out of the deck"
          " you will be given the choice between 1 and"
          " 11 to allocate its value.")
    sleep(1)
    answer_play = input("Would you like to see the cards? \n")
    if positive_feedback(answer_play=answer_play):
        print("Here are your cards: ")
        sleep(1)
        for list_of_dicts_in_cards in cards():
            print(list_of_dicts_in_cards['card_type'], end=' ')
            print(f"of value {list_of_dicts_in_cards['card_value']}")
            print(list_of_dicts_in_cards['card_art'])
            sleep(2)


# BlackjackGame.processor()
