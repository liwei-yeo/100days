from replit import clear
import random
from Day7_2_hangman_words import word_list
import Day7_1_hangman_art
# from Day7_1_hangman_art import stages, logo

#chosen_word = random.choice(word_list)
chosen_word = word_list[random.randint(0,len(word_list) -1)]
#print(chosen_word)

display = []
for char in chosen_word:
    display += "_"

end_of_game = False
lives = 6

print(Day7_1_hangman_art.logo)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
        print(f"You've already guessed '{guess}'.")
    else:
        # for position in range(len(word_list)):
        #     letter = chosen_word[position]
        #     if letter == guess:
        #         display[position] = letter
        pos = 0
        for char in chosen_word:
            if char == guess:
                display[pos] = char
            pos += 1

        if guess not in chosen_word:
            lives -= 1
            print(f"'{guess}' is not in the word. You lose a life.")
            if lives == 0:
                end_of_game = True
                print(f"The word is {chosen_word}.\nYou lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(Day7_1_hangman_art.stages[lives])
