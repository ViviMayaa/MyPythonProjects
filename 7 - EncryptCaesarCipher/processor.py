# the amount chosen shifts the alphabet to that extend
import string

print("""          
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")


def caeser_cipher():
    cipher_base = []
    cipher_base += [elements for i, elements in enumerate(string.ascii_letters) if i < 26]
    # [x for x in range(10) if x < 5]
    # newlist = [x for x in fruits if "a" in x]
    # cipher_base.append(string.ascii_letters[0:26])

    chosen_type = input('Type "encode" to encrypt and "decode" to decrypt: ').lower().strip()
    if not (chosen_type == "encode" or chosen_type == "decode"):
        print("Invalid input, try again.")
        caeser_cipher()
    if chosen_type == "encode":
        encoded_message = []
        message = input("Please type your message: ").lower().strip()

        try:
            chosen_ciper = int(input("Please choose a cipher number: "))
        except ValueError:
            print("Please type a number for the cipher.")

        for letters in message:
            for i, words in enumerate(cipher_base):

                if words == letters:
                    encoded_message.append(cipher_base[i + chosen_ciper])

        print(f"Your decoded message is: {''.join(map(str, encoded_message))}")
    if chosen_type == "decode":
        encoded_message = []
        message = input("Please type your message: ").lower().strip()

        try:
            chosen_ciper = int(input("Please choose a cipher number: "))
        except ValueError:
            print("Please type a number for the cipher.")

        for letters in message:
            for i, words in enumerate(cipher_base):
                if words == letters:
                    encoded_message.append(cipher_base[i - chosen_ciper])

        print(f"Your encoded message is: {''.join(map(str, encoded_message))}")


caeser_cipher()

play_again = input("Want to ciper again? Yes or no?\n").lower().strip()
if play_again == 'yes':
    caeser_cipher()
else:
    print("Thank you for using!")
    quit()



