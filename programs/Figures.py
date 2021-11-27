# Copyright
__author__ = "Danny Sequeira"
__copyright__ = "Copyright (C) 2021 Danny Sequeira"


# Methods
def print_figure1():
    figure1 = [
        "**********",
        "*        *",
        "*        *",
        "*        *",
        "*        *",
        "*        *",
        "*        *",
        "*        *",
        "**********"
    ]

    for i in range(0, len(figure1)):
        print(figure1[i])


def print_figure2():
    figure2 = [
        "   +   ",
        "   **  ",
        "  o**o ",
        " **o**o",
        " *o**o**",
        "o*o**o*o",
        "   ||   "
    ]

    for i in range(0, len(figure2)):
        print(figure2[i])


def print_figure3():
    figure3 = [
        "1  00000    1",
        "1  0   0    1",
        "1  0   0 == 1",
        "1  0   0    1",
        "1  00000    1"
    ]

    for i in range(0, len(figure3)):
        print(figure3[i])


# switch
switch_print_figures = {
    1: print_figure1,
    2: print_figure2,
    3: print_figure3
}


def start_program():
    print("Bienvenido al programa Figuras: ")

    should_continue = True
    while should_continue:

        num1 = int(input("Cual figura desea imprimir (del 1 al 3): "))
        switch_print_figures.get(num1, "Error")()

        user_decision = int(input("Desea volver a imprimir otra figura? (1. si, 2. no): "))
        if user_decision == 2:
            should_continue = False
            print("Le deseamos exitos en sus labores")
        elif user_decision == 1:
            print("Perfecto, volvamos al principio")
        else:
            print("Opción invalida, por eso seguiremos con el programa")
