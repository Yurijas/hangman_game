# output() function
from IPython.display import clear_output
# get random word from the word list
import random

# wordlist
word_list =["horse", "cheese", "truck", "computer", "building", "juice", "pinapple", "desktop",
 "laptop", "penguin", "rabbit", "lemon", "orange", "tree", "phone"]
# word the user need to guess
secret_word = random.choice(word_list)
# stock the right-guessed letters and make it comperable to secret_word
guessed_word = []

# TODO 1: make it like l_p__p (start from ________ and goes raccoon or something)
# TODO 2: (in the future) if same letter was typed, using letter_storage = [] or something and show "You already typed the letter."


# HANGMAN GAME PLAYED ON
def hangmanOn():
    remained_count = int(7)

    while True:
        guessed_letter = input("Please guess and type an alphabet. The word has {} letters.".format(len(secret_word)))

        # Correct Guess  (make rightAns() outside?)
        if guessed_letter.lower() in secret_word:
            guessed_word.append(guessed_letter.lower())
            clear_output()
            print("Your guess '{}' is correct! Keep going.".format(guessed_letter))
            # trying to put "-" things
            # for guessed_letter in set(secret_word):
            blanks = list("_"*len(secret_word))
            blanks = [guessed_letter if letter == guessed_letter else blank
                      for blank, letter in zip(blanks, secret_word)]
            print("".join(blanks))
        # Wrong Guess  (make wrongAns() outside?)
        elif guessed_letter.lower() not in secret_word:
            remained_count -= 1
            if remained_count != 0:
                clear_output()
                print("Your guess '{}' is wrong! Try again.".format(guessed_letter))
                print("You have {} chances left.".format(remained_count))
            elif remained_count == 0:
                clear_output()
                print("Game over! The word was {}.".format(secret_word))
                break
        # In case of typo or something
        else:
            clear_output()
            print("Please type an alphabet again.")
        # check for win condition here
        for char in secret_word: # loop through each letter in the secret_word
            if char not in guessed_word: # see if the letter is in the guessed_word list
                break
        else: # run if the for loop doesn't break
            clear_output()
            print("Congratuation!! You got the word right!")
            break

# HANGMAN GAME MAIN
def hangmanGame():
    remained_count = int(7)
    while True:
        ans = input("Please type 'start' or 'quit'.")
        # start hangman
        if ans.lower() == "start":
            clear_output()
            print("You have {} chances.".format(remained_count))
            hangmanOn()
        # finish hangman
        elif ans.lower() == "quit":
            clear_output()
            print("Thank you for playing!")
            break
        else:
            print("Sorry could you type again?")

hangmanGame()
