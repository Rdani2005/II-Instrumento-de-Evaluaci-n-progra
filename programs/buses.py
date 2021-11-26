import random

# Copyright
__author__ = "Danny Sequeira"
__copyright__ = "Copyright (C) 2021 Danny Sequeira"

prices = [
    3500,  # Jorney to puntarenas
    5000,  # Jorney to Parrita
    6000,  # Journey to Quepos
    8000   # Journey to Manuel Antonio
]

bus = [
    "Puntarenas",
    "Parrita",
    "Quepos",
    "Manuel Antonio"
]

used_sits = []


def welcome():
    print("Qué bus desea tomar?")
    for i in range(0, len(prices)):
        print(f"{i + 1}. Bus camino a {bus[i]} con precio de {prices[i]} colones")

    return int(input("Escoja una opción (del 1 al 4: "))


def amount_buses(used_bus):
    used_bus -= 1
    bus_price = prices[used_bus]
    tickets = int(input("Cuantos ticketes desea?"))
    total_price = bus_price * tickets
    hour = int(input("A que hora realizó su compra? (favor digitar de 6 a 19 horas)"))
    
    is_incorrect_hour = True
    while is_incorrect_hour:
        if hour < 6 or hour > 19:
            print("El horario es incorrecto. intente nuevamente")
        else:
            is_incorrect_hour = False
            if hour % 2 == 0:
                print("Perfecto, su bus está a punto de salir")
            else:
                print("Perfecto, su bus sale cada dos horas, por tal motivo, sale en 1 hora")
    for i in range(0, tickets):

        is_occupied = True
        while is_occupied:
            sit_down = random.randint(1, 42)
            if sit_down in used_sits:
                is_occupied = True
            else:
                is_occupied = False

        print(f"El ticket {i} es del asiento {sit_down}")
    return total_price


def counters():
    # Counters
    counter_bus1 = 0
    counter_bus2 = 0
    counter_bus3 = 0
    counter_bus4 = 0
    # Earned
    earned_bus_1 = 0
    earned_bus_2 = 0
    earned_bus_3 = 0
    earned_bus_4 = 0
    should_continue = True

    while should_continue:
        print("Bienvenido a La terminal de Bus de Puntarenas!!!")
        used_bus = welcome()
        earned_bus = amount_buses(used_bus)

        if used_bus == 1:
            counter_bus1 += 1
            earned_bus_1 += earned_bus
        elif used_bus == 2:
            counter_bus2 += 1
            earned_bus_2 += earned_bus
        elif used_bus == 3:
            counter_bus3 += 1
            earned_bus_3 += earned_bus
        elif used_bus == 4:
            counter_bus4 += 1
            earned_bus_4 += earned_bus

        user_decision = int(input("Desea continuar (1. Si 2. No)"))
        if user_decision == 1:
            should_continue = True
        else:
            should_continue = False

    print(f"El total ganado por el bus 1 es: {earned_bus_1}")
    print(f"El total ganado por el bus 2 es: {earned_bus_2}")
    print(f"El total ganado por el bus 3 es: {earned_bus_3}")
    print(f"El total ganado por el bus 4 es: {earned_bus_4}")


def start_program():
    print("Bienvenido al programa Buses: ")

    should_continue = True
    while should_continue:

        user_decision = int(input("Desea volver a correr el programa? (1. si 2.no): "))
        if user_decision == 2:
            should_continue = False
            print("Le deseamos exitos en sus labores")
        elif user_decision == 1:
            print("Perfecto, volvamos al principio")
        else:
            print("Opción invalida, por eso seguiremos con el programa")


