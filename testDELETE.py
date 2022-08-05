import string
wrong_attempt_format = False
word_attempt ='2'
print(string.punctuation)
for i, elements in enumerate(string.digits or string.punctuation):
    if word_attempt == elements:
        wrong_attempt_format = True