def print_hangman(num_wrong_guesses):
    print("  ____")
    print("  |  |")

    if num_wrong_guesses == 0:
        print("     |")
        print("     |")
        print("     |")
        print("     |")
    elif num_wrong_guesses == 1:
        print("  O  |")
        print("     |")
        print("     |")
        print("     |")
    elif num_wrong_guesses == 2:
        print("  O  |")
        print("  |  |")
        print("     |")
        print("     |")
    elif num_wrong_guesses == 3:
        print("  O  |")
        print(" /|  |")
        print("     |")
        print("     |")
    elif num_wrong_guesses == 4:
        print("  O  |")
        print(" /|\\ |")
        print("     |")
        print("     |")
    elif num_wrong_guesses == 5:
        print("  O  |")
        print(" /|\\ |")
        print(" /   |")
        print("     |")
    else:
        print("  O  |")
        print(" /|\\ |")
        print(" / \\ |")
        print("     |")

    print("_____|___")
