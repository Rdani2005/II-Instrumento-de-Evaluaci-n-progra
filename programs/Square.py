import math

# Copyright
__author__ = "Danny Sequeira"
__copyright__ = "Copyright (C) 2021 Danny Sequeira"


def square_root(num):
    num = math.sqrt(num)
    return num


def power_num(num):
    num = num ** 2
    return num


def compare_pair_odds():
    num = int(input("Ingrese un numero: "))
    if num % 2 == 0:
        print(f"El numero {num} es par, y su raíz es: {square_root(num)}")

    else:
        print(f"El numero {num} es impar, y su potencia a la 2 es: {power_num(num)}")


# # start the program
def start_program():
    print("Bienvenido al programa Raices y Potencias: ")
    should_continue = True
    while should_continue:
        compare_pair_odds()
        user_decision = int(input("Desea ingresar otro numero: "))
        if user_decision == 2:
            should_continue = False
            print("Le deseamos exitos en sus labores")
        elif user_decision == 1:
            print("Perfecto, volvamos al principio")
        else:
            print("Opción invalida, por eso seguiremos con el programa")


