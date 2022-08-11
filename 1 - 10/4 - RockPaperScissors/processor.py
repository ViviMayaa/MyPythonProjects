import random
tries = True
your_point = 0
computer_point = 0
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

while tries:
    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    # random.randint(0, 3)
    computer_choice = random.randrange(0, 3, 1)
    # win 0 - 2, 1 - 0, 2 - 1
    # lose 0 - 1, 1 - 2, 2 - 0

    print("Your choice:\n")
    if player_choice == 0:
        print(rock)
    elif player_choice == 1:
        print(paper)
    else:
        print(scissors)
    print("Against the computer choice:\n")
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    else:
        print(scissors)

    if (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) \
            or (player_choice == 2 and computer_choice == 1):
        print("\nYou won!")
        your_point += 1
    elif (player_choice == 0 and computer_choice == 1) or (player_choice == 1 and computer_choice == 2) \
            or (player_choice == 2 and computer_choice == 0):
        print("\nYou lost!")
        computer_point += 1
    elif player_choice == computer_choice:
        print("\nIs a draw!")

    print(f"You {your_point} X {computer_point} Computer ")
