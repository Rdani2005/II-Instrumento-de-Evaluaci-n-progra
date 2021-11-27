# Copyright
__author__ = "Danny Sequeira"
__copyright__ = "Copyright (C) 2021 Danny Sequeira"

pair_list = []

odd_list = []

num_list = []


# Methods
# # Says if the num is pair or not
def compare_nums():

    for i in range (0, 10):
        num = int(input("Ingrese un numero: "))
        num_list.append(num)
        if num % 2 == 0:
            print("El numero es par.")
            pair_list.append(num)
        elif num % 2 != 0:
            print("El numero es impar")
            odd_list.append(num)


# # Print the list of numbers
def print_list():
    print("La lista de numero ingresados es: ")
    print(num_list)
    print("La lista de numeros pares ingresados es: ")
    print(pair_list)
    print("La lista de numeros impares ingresados es: ")
    print(odd_list)


# # start the program
def start_program():

    print("Bienvenido al programa Lista Pares e Impares: ")
    should_continue = True
    while should_continue:
        pair_list.clear()
        odd_list.clear()
        compare_nums()
        print_list()
        user_decision = int(input("Desea insetar otra lista de numeros (1.si 2.no): "))
        if user_decision == 2:
            should_continue = False
            print("Le deseamos exitos en sus labores")
        elif user_decision == 1:
            print("Perfecto, volvamos al principio")
            pair_list.clear()
            odd_list.clear()
            num_list.clear()
        else:
            print("Opción invalida, por eso seguiremos con el programa")
            pair_list.clear()
            odd_list.clear()
            num_list.clear()
