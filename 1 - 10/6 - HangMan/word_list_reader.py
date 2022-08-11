import random


class WordListReader:

    @classmethod
    def word_list(cls):
        with open("WordList", 'r') as words_draft:
            words_list = words_draft.read().split(",")
        return words_list

    @classmethod
    def random_word(cls):
        words = cls.word_list()
        chosen_word = random.choice(words)
        # chosen_word = words[random.randint(0, len(words) - 1)]
        return chosen_word
