import calendar
# Copyright
__author__ = "Danny Sequeira"
__copyright__ = "Copyright (C) 2021 Danny Sequeira"


# Method to print the calendar
def print_calendar():
    cl = calendar.TextCalendar()
    month = int(input("Cual es el mes que desea imprimir (del 1 al 12 unicamente): "))
    year = int(input("Cual es el año que desea imprimir: "))
    calendar_to_print = cl.formatmonth(year, month)
    print(calendar_to_print)


# Method to start the program
def start_program():
    print("Bienvenido al programa Calendario: ")
    should_continue = True

    while should_continue:
        print_calendar()
        user_decision = int(input("Desea volver a imprimir otro calendario? (1. si, 2. no): "))
        if user_decision == 2:
            should_continue = False
            print("Le deseamos exitos en sus labores")
        elif user_decision == 1:
            print("Perfecto, volvamos al principio")
        else:
            print("Opción invalida, por eso seguiremos con el programa")


