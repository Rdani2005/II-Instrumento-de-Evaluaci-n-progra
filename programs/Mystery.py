# Copyright
__author__ = "Danny Sequeira"
__copyright__ = "Copyright (C) 2021 Danny Sequeira"


def misterio(num1, num2):
    operation = int(input("Que operación desea Realizar con los numeros (1. Suma, 2.Resta, 3.Multiplicación, 4. División): "))
    if operation == 1:
        result = num1 + num2
    elif operation == 2:
        result = num1 - num2
    elif operation ==  3:
        result = num1 * num2
    elif operation == 4:
        result = num1 / num2
    else:
        print("Error, opción incorrecta. Vuelva a intentarlo!!!")
    print(f"El resultado de su operación es {result}")


def start_program():
    print("Bienvenido al programa Misterio: ")

    should_continue = True
    while should_continue:

        num1 = int(input("Por favor, ingrese un numero: "))
        num2 = int(input("Por favor, ingrese otro numero: "))
        misterio(num1, num2)

        user_decision = int(input("Desea volver al inicio de Misterio? (1. si, 2. no): "))
        if user_decision == 2:
            should_continue = False
            print("Le deseamos exitos en sus labores")
        elif user_decision == 1:
            print("Perfecto, volvamos al principio")
        else:
            print("Opción invalida, por eso seguiremos con el programa")


