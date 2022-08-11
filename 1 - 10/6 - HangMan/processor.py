from word_list_reader import WordListReader
from images import hang_man_title, hang_base, hang_first_mistake, hang_second_mistake, hang_third_mistake, \
    hang_fourth_mistake, hang_fifth_mistake, hang_six_mistake, hang_last_mistake, won
import string


def hang_man_game():
    print("Welcomed to the Hangman game!")
    hang_man_title()
    tries = 7
    random_word = WordListReader.random_word()

    # cheating to test
    # print(random_word)
    lines_random_word = words_lines(random_word)
    hang_base()
    attempts_tried = []

    while tries != 0:
        right = False
        print(' '.join(map(str, lines_random_word)))

        # winning condition
        if (''.join(map(str, lines_random_word))) == random_word:
            print("~~ You've won! Congrats! ~~")
            won()
            break
        word_attempt = input("Type a word: \n").lower().strip()

        wrong_attempt_format = word_attempt_format_check(attempts_tried, word_attempt)
        attempts_tried += word_attempt

        # word is right
        for i, elements in enumerate(random_word):
            if word_attempt == elements:
                lines_random_word = adding_words_to_line(lines_random_word, word_attempt, i)
                right = True

        # word is wrong
        if not right and not wrong_attempt_format:
            print("~~ You got it wrong! ~~")
            tries -= 1
            print_hang_man(tries)
            continue

    # losing condition
    if tries == 0:
        print("~~You lost!~~")
        print(f"The word was: {random_word}")
        hang_last_mistake()


def words_lines(random_word):
    lines_random_word = []
    for elements in range(len(random_word)):
        lines_random_word += "_"
    return lines_random_word


def adding_words_to_line(lines_random_word, word_attempt, i):
    lines_random_word[i] = word_attempt
    return lines_random_word


def print_hang_man(tries):
    if tries == 6:
        hang_first_mistake()
    elif tries == 5:
        hang_second_mistake()
    elif tries == 4:
        hang_third_mistake()
    elif tries == 3:
        hang_fourth_mistake()
    elif tries == 2:
        hang_fifth_mistake()
    elif tries == 1:
        hang_six_mistake()


def word_attempt_format_check(attempts_tried, word_attempt):
    # format words treatment
    wrong_attempt_format = False
    for words in attempts_tried:
        if word_attempt == words:
            print("You've already tried that letter, chose another one.")
            wrong_attempt_format = True
            break
    if len(word_attempt) > 1:
        print("One word per try.")
        wrong_attempt_format = True

    not_allowed_elements = string.digits + string.punctuation
    for i, elements in enumerate(not_allowed_elements):
        if word_attempt == elements:
            print("Word attempted is not a letter, try again.")
            wrong_attempt_format = True
            break
    if word_attempt.strip() == "":
        print("Empty is not valid, try again.")
        wrong_attempt_format = True

    return wrong_attempt_format


hang_man_game()

play_again = input("Want to play again? Yes or no?\n").lower().strip()
if play_again == 'yes':
    hang_man_game()
else:
    print("Thank you for playing!")
    quit()



