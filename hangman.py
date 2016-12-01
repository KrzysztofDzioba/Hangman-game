import random
import sys
capitals = ["TIRANA", "ANDORRA LA VELLA", "YEREVAN", "VIENNA", "BAKU", "MINSK",
"BRUSSELS", "SARAJEVO", "SOFIA", "ZAGREB", "NICOSIA", "PRAGUE", "COPENHAGEN",
"TALLINN", "HELSINKI", "PARIS", "TBILISI", "BERLIN", "ATHENS", "BUDAPEST",
   "REYKJAVIK", "DUBLIN", "ROME", "ASTANA", "PRISTINA", "RIGA", "VADUZ",
    "VILNIUS", "LUXEMBOURG", "SKOPJE", "VALLETTA", "CHISINAU", "MONACO",
     "PODGORICA", "AMSTERDAM", "OSLO", "WARSAW", "LISBON", "BUCHAREST",
      "MOSCOW", "SAN MARINO", "BELGRADE", "BRATISLAVA", "LJUBLJANA", "MADRID",
       "STOCKHOLM", "BERN", "ANKARA", "KYIV", "LONDON"]


capital = random.choice(capitals)
count_capital = len(capital)
dash_list = [" _ "] * count_capital
bad_list = []
life = 5

if " " in capital:
    for index3, value3 in enumerate(list(capital)):
        if value3 == " ":
            dash_list[index3] = " "

print ("\n \nWelcome in Hangman game!\n")

def letter():
    """Checks if user's letter is correct."""
    global life
    letter = input("\nPlease type your letter: ")
    letter = letter.upper()
    print("\n \nYou typed " + letter + ".")
    if letter in list(capital):
        print("\nThis letter is in my capital!\n")
        for index, value in enumerate(list(capital)):
            if value == letter:
                dash_list[index] = letter
        if dash_list == list(capital):
            print("\n****************Correct! You won!****************\n")
            sys.exit()
        for p in dash_list:
            print(p, end="")
        main()
    else:
        print("\nThere is no " + letter + " in my capital.\n")
        if letter not in list(capital):
            life -= 1
        print ("\nYou lost one life. You still have " + str(life) + " lives.\n")
        bad_list.append(letter)
        print("List of letters that are not in my capital:")
        print(bad_list)
        main()


def word():
    """Checks if user's word (capital) is correct."""
    global life
    word = input("\nPlease type in the word: ")
    word = word.upper()
    if word == capital:
        print("\nYes! You guessed the capital. You won!\n")
    else:
        life = life - 1
        print ("\nYou lost one life. You have " + str(life) + " lives.")
        main()


def main():
    """Checks if user wants to type letter or word"""
    global life
    if life == 0:
        print("You are hanging!")
        sys.exit()
    l_or_w = input("\n \nPlease choose letter (l) or word (w): ")
    if l_or_w == "l":
        letter()
    elif l_or_w == "w":
        word()

    elif l_or_w == "b":  # That's a cheat!
        print("\n*************************Cheater on board!********************\
*****\nMy capital is: ")
        print(capital)
        main()

    else:
        print("\nPlease choose l or w")
        main()


main()
