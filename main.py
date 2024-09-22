#Importing random module and the word list from hangman_word
import random
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#prints logo (duh)
from hangman_art import logo
print(logo)



display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    
    if guess in display:
        print("you have already guessed this letter.")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    #If player chooses wrongly
    if guess not in chosen_word:
        
        print("Letter is not in chosen word, you lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String
    print(f"{' '.join(display)}")

    
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Imports the hangman stages from hangman_art
    from hangman_art import stages 
    print(stages[lives])
