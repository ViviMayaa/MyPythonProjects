import pandas as pd
import string

nato_dict_frame = pd.read_csv("nato_phonetic_alphabet.csv")
# nato_dict = nato_dict_frame.set_index('letter').to_dict()
# nato_dict = nato_dict['code']


def verifying_error(player_answer):
    try:
        output_list = [nato_dict[letter] for letter in player_answer]
    except KeyError as error:
        raise KeyError(f"Value {error} must be a letter.")


nato_dict = {row.letter: row.code for (index, row) in nato_dict_frame.iterrows()}
result = []
player_answer = input("Please insert the word: ").upper()
verifying_error(player_answer)

for word_answer in player_answer:
    result += [nato_dict[element] for element in nato_dict if element in word_answer]
print(result)


# Second way of handling error
# for word_answer in player_answer:
#     list_of_letters = ''
#     for letters in string.ascii_uppercase:
#         if letters == word_answer:
#             list_of_letters = word_answer
#     if list_of_letters == '':
#         raise ValueError(f"Value {word_answer} must be a letter.")
#     result += [nato_dict[element] for element in nato_dict if element in word_answer]
# print(result)
