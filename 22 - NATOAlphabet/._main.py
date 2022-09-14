import pandas as pd

nato_dict_frame = pd.read_csv("nato_phonetic_alphabet.csv")
# nato_dict = nato_dict_frame.set_index('letter').to_dict()
# nato_dict = nato_dict['code']
print(nato_dict_frame.iterrows())
nato_dict = {row.letter: row.code for (index, row) in nato_dict_frame.iterrows()}
result = []
player_answer = input("Please insert the word: ").upper()
for word_answer in player_answer:
    result += [nato_dict[element] for element in nato_dict if element in word_answer]
print(result)