from hangmanfunctions import print_hangman
import random
import itertools
count = 0
hangman_words = open("words for hangman.txt")
words = []
for line in hangman_words:
    line = line.rstrip()
    words.append(line.split())
single_words = list(itertools.chain(*words))


print("\nWhile searching for the treasure in one of the big dark caves, you have encountered a big stone figure asking you to play hangman with him.\n")
user_first = input("Big Stone Figure:\nWill you play Hangman with me, if you win i will give you a map for the treasure you were looking for. Just say Yes or No.\n")

if user_first == "Yes" or user_first == "yes":
    user_name = input("Say your name dear traveler...\n")
    selected_word = random.choice(single_words)
    guessed_letters = []
    lives = 6
    while True:
        status = ""
        for letter in selected_word:
            if letter in guessed_letters:
                status += letter
            else:
                status += "_"
        print(status)

        guess = input("Guess a letter traveler...\n")

        if guess in selected_word:
            guessed_letters.append(guess)
            print("Correct one, hah lucky guess.")
        else:
            count += 1
            lives -= 1
            print("Ugh, what a shame...")
            print(f"You still have {lives} lives left.")
            print_hangman(count)
        if all(letter in guessed_letters for letter in selected_word):
            print("Huh, impressive, very impressive, you've won.")
            print(f"Here is your map traveler, {user_name}.\n")
            break
        elif lives == 0:
            print("I am not so sorry about this haha.")
            print(f"The word was {selected_word}.")
            print("Now i get to collect your head.")
            break

elif user_first == "no" or user_first == "No":
    print("Goodbye then, your loss.")
    quit()
