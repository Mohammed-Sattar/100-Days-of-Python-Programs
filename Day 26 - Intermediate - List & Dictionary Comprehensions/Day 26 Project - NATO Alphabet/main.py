import pandas

nato_alphabet_data = pandas.read_csv(r"Day 26 - Intermediate - List & Dictionary Comprehensions\Day 26 Project - NATO Alphabet\nato_phonetic_alphabet.csv")


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:   {"A": "Alfa", "B": "Bravo"}
nato_alphabet_dict = {row.letter:row.code for (index, row) in nato_alphabet_data.iterrows()}
# print(nato_alphabet_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()

word_nato_alphabet = [nato_alphabet_dict[letter] for letter in user_word]
print(word_nato_alphabet)
