from random import *


class PasswordGenerator:
    def __init__(self):
        # Initialize the list of possible characters for password generation.
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']\

        # List of numbers that can be included in the password.
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        # List of symbols that can be included in the password.
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        # Initialize counters for the number of each type of character to include in the password.
        self.nr_letters = 0
        self.nr_symbols = 0
        self.nr_numbers = 0
    def pass_making(self):
        # Generate lists of random characters based on user input counts.
        pass_letter = [choice(self.letters) for letter in range(0, self.nr_letters) ]
        pass_symbol = [choice(self.symbols) for symbol in range(0, self.nr_symbols)]
        pass_nmber = [choice(self.numbers) for number in range(0, self.nr_numbers)]

        # Combine all character lists into a single list.
        new_pass = pass_letter + pass_symbol + pass_nmber

        # Shuffle the combined list to randomize character positions.
        shuffle(new_pass)
        password = "".join(new_pass)

        # Return the generated password.
        return password
