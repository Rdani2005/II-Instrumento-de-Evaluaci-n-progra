# Libraries!!!
import random
# # To be honest, I used this library just for fun
import time


# Copyright
__author__ = "Danny Sequeira"
__copyright__ = "Copyright (C) 2021 Danny Sequeira"


# This is just the list of words that the game includes
words_list = [
    "hola",
    "vida",
    "python",
    "ahorcado",
    "danny",
    "profesor",
    "archivo"
]
#    ^
#    |
# We can use the split method, but I prefer to create the list of words
# Instead of using that method. I think that's just choices.

# This are just the letters that the user has already introduced
introduced_letters = []
# This are just the letters thar are part of the word
right_letters = []


# Body
def print_budy(num):
    dead_body = [
        [
            "========",
            "|     | ",
            "|     0 ",
            "|    /|\\",
            "|     | ",
            "|    / \\",
        ],
        [
            "========",
            "|     | ",
            "|     0 ",
            "|    /|\\",
            "|     | ",
            "|       ",
        ],

        [
            "========",
            "|     | ",
            "|     0 ",
            "|    /|\\",
            "|       ",
            "|       ",

        ],
        [
            "========",
            "|     | ",
            "|     0 ",
            "|    /| ",
            "|       ",
            "|       ",

        ],
        [
            "========",
            "|     | ",
            "|     0 ",
            "|       ",
            "|       ",
            "|       ",

        ],
        [
            "========",
            "|     | ",
            "|       ",
            "|       ",
            "|       ",
            "|       ",
        ]
    ]

    for j in dead_body[num]:
        print(j)


# Method to say Hello! to the user
def welcome():
    print("Bienvenido al Juego del Ahorcado!!!")
    time.sleep(2)
    print("Vamos a adivinar una palabra entera. Tienes 5 intentos, lo que significa que si fallas 5 veces, Pierdes!!")


# Return if the user has enter a letter or not
def is_a_letter(letter):
    if (len(letter) != 1) or (letter.isnumeric()):
        print(f"Lo ingresado por el usuario: {letter}, no es una letra. Por favor, digite una letra")
        return True

    else:
        is_on_list(letter)


# Has the user typed the letter already?
def is_on_list(letter):
    if letter.lower() in introduced_letters:
        print("La letra ya ha sido escogida. Vuelva a intentarlo")
        return True
    else:
        return False


# Let's build the game!
def play_game():
    # Amount of opportunities
    life = 5
    # Define the world from the list, using random Library
    guess_word = random.choice(words_list)
    continue_playing = True
    # Play the game
    while continue_playing:
        is_incorrect = True
        # This while is used to see if the letter is a letter or is on the list
        while is_incorrect:
            letter = input("Por favor, ingresa una letra: ")
            is_incorrect = is_a_letter(letter)
        # Ask if the letter is on the world
        if letter.lower() in guess_word:
            print("Letra correcta!!!")
            introduced_letters.append(letter)
            right_letters.append(letter)
        else:
            print("Lo sentimos... Letra errada.")
            introduced_letters.append(letter)
            life -= 1
        # Let's see if there are more opportunities for the user
        if life == 0:
            continue_playing = False
            print("Te quedaste sin vidas!!! Has perdido el juego!")
            time.sleep(5)
        # Let's print a dead body
        print_budy(life)
        # Let's see the status of the game
        status = ""
        missing = 0
        for i in guess_word:
            if i in right_letters:
                status += i
            else:
                status += "_"
                missing += 1

        print(f"El estado actual de la palabra es: {status}")
        # Has the user win?
        if missing == 0:
            print("Felicidades!!! Ha ganado el juego!!")
            continue_playing = False

        else:
            print(f"Te faltan {missing} letras")
        time.sleep(5)


# Method to start the game
def start_program():
    welcome()
    should_continue = True
    # Should we play the game a lot of times?
    while should_continue:
        play_game()
        introduced_letters.clear()
        right_letters.clear()
        time.sleep(5)
        user_decision = int(input("Desea jugar otra vez? (1. si, 2. no): "))
        if user_decision == 2:
            should_continue = False
            print("Le deseamos exitos en sus labores")
        elif user_decision == 1:
            print("Perfecto, volvamos al principio")
        else:
            print("Opción invalida, por eso seguiremos con el programa")


