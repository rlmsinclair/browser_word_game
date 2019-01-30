import random


class CurrentLetters:

    current_letters = ''

    def __init__(self):
        self.current_letters = CurrentLetters.get_random_letter()

    @staticmethod
    def get_random_letter():
        random_number = random.randint(0, 25)
        random_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[random_number]
        return random_letter

    def add_letter_to_back(self, letter):
        self.current_letters = self.current_letters + letter

    def add_letter_to_front(self, letter):
        self.current_letters = letter + self.current_letters

    def get_letters(self):
        return self.current_letters
