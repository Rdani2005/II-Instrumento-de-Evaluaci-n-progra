# Copyright
__author__ = "Danny Sequeira"
__copyright__ = "Copyright (C) 2021 Danny Sequeira"


def invest_cad():
    my_cad = input("Escribe una palabra, una frase o oración")
    print(f"El texto ingresado: {my_cad} invertido quedaría {my_cad[::-1]}")


# Method to start the program
def start_program():
    print("Bienvenido al programa Reverso de la Palabra: ")
    should_continue = True

    while should_continue:
        invest_cad()
        user_decision = int(input("Desea volver a invertir otra palabra? (1. si, 2. no): "))
        if user_decision == 2:
            should_continue = False
            print("Le deseamos exitos en sus labores")
        elif user_decision == 1:
            print("Perfecto, volvamos al principio")
        else:
            print("Opción invalida, por eso seguiremos con el programa")


