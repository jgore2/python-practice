import random
from words_file import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what user has already guessed

    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        if lives > 1:
            print('You have ' , lives, 'lives left and have used these letters: ', ' '.join(used_letters))
        else:
            print('Watch out! You have 1 life left and have used these letters: ', ' '.join(used_letters))
        
        # current correct letters
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input('Guess a letter:').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 # takes away a life if wrong letter guessed

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid character. Please try again.')

    #gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('Sorry, you died. The word was', word)
    else:
        print('You guessed the word ', word, 'correctly!!')

hangman()
#user_input = input('Type something')
#print(user_input)   
