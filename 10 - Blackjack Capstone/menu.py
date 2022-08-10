from time import sleep
from processor import BlackjackGame
from art import ArtModels
from useful import positive_feedback


print("Welcome to...")
sleep(2)
ArtModels.the_art()
sleep(1)
ArtModels.logo_art()
sleep(1)
ArtModels.game_art()
sleep(1)

answer_play = input("Would you like to play? ").lower()
if positive_feedback(answer_play=answer_play):
    BlackjackGame.start_blackjack()
else:
    print("Thank you for playing! ")
