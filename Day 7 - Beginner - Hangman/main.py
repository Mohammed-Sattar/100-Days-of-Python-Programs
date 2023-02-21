import random
import hangman_art
import hangman_words

print(hangman_art.logo)
# STEP 1:
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(hangman_words.word_list)
# print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# Edit: This TODO was replaced with 3rd part TODO-1

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. 
# Edit: This TODO was replaced with 2nd part TODO-2

# STEP 2:
#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for _ in chosen_word:
    display += "_"
print(display)

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
# Edit: This TODO was replaced with 3rd part TODO-1


#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
# Edit: This TODO was replaced with 3rd part TODO-1

# STEP 3:
#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the 
# chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
# Edit: This TODO was replaced with 4th part TODO-2


#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#TODO-2: - If guess is not a letter in the chosen_word,
#Then reduce 'lives' by 1. 
#If lives goes down to 0 then the game should stop and it should print "You lose."
guess = ""
while True : #"_" in display:
    guess = input("Guess a letter:\n").lower()

#TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    if guess in display:
        print(f"You have already guessed the letter {guess}")

    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            display[position] = guess

#TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.

    if guess not in (chosen_word):
        print(f"{guess} is not in the word")
        lives -= 1  

    # print(display)
    print(" ".join(display))
    print(hangman_art.stages[lives])

    if lives <= 0:
        print("You lose.")
        break; 
    
    if "_" not in display:
        print("".join(display))
        print("You've won!")
        break;
    

#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

