import pandas

# 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("Day26_nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato_dict)

# 2. Create a list of the phonetic code words from a word that the user inputs.

def nato():
    word = input("Enter a word: ")
    try:
        result = [nato_dict[letter.upper()] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabets please.")
        nato()
    else:
        print(result)

nato()
