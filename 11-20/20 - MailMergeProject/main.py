# TODO: Create a letter using starting_letter.txt
list_letters = ''
with open("../20 - MailMergeProject/Input/Letters/starting_letter.txt") as letter:
    letter = letter.read()
    with open("../20 - MailMergeProject/Input/Names/invited_names.txt") as name_list:
        name_list = name_list.readlines()
        for name in name_list:
            name = name.strip()
            list_letters = letter.replace("[name]", name)
            with open(f"../20 - MailMergeProject/Output/ReadyToSend/LetterTo{name}.txt", 'w') as writing_letter:
                writing_letter.write(list_letters)

# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
