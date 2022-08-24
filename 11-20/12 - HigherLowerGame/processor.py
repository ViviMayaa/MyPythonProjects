import art
import game_data
import random
# compare both options and the one higher is the correct one
print(art.logo)


def start():
    option_a = random.choice(game_data.data)
    option_b = random.choice(game_data.data)
    score = 0
    if option_a == option_b:
        option_b = random.choice(game_data.data)
    game(option_a, option_b, score)


def game(option_a, option_b, score):

    print(f"Compare A: {option_a['name']}, a {option_a['description']} from {option_a['country']}.")
    print(art.vs)
    print(f"Against B: {option_b['name']}, a {option_b['description']} from {option_b['country']}\n")
    player_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if player_choice == 'A':
        player_choice = option_a
        opponent = option_b
    elif player_choice == 'B':
        player_choice = option_b
        opponent = option_a
    else:
        print('Please type a available input. ')
        game(option_a, option_b, score)

    if player_choice['follower_count'] > opponent['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}\n")
        option_a = option_b
        option_b = random.choice(game_data.data)
        game(option_a, option_b, score)

    else:
        print("You got it wrong! ")
        quit()


start()
