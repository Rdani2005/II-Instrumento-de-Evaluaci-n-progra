# Data from other files
from programs import PairOdds as ListPairsAndOdds, DeadBody as DeadBodyGame, buses as BusStation, \
    Square as PrintSquares, Tables as PrintTables, CalendarIdea, Mystery as MisteryProgram, Figures as PrintFigures, \
    WordReverse as WordReverse

# Copyright
__author__ = "Danny Sequeira"
__copyright__ = "Copyright (C) 2021 Danny Sequeira"

# Method to say Hi to the user, and ask the program that wants to use
def welcome():
    print("Bienvenido al Instrumento II ")
    print("1.   Calendario")
    print("2.   Misterio")
    print("3.   Figuras")
    print("4.   Pares e Impares")
    print("5.   Raices y Potencias")
    print("6.   Reverso de la palabra")
    print("7.   Tablas de Verdad")
    print("8.   Juego Ahorcado")
    print("9.   Para de Buses a Puntarenas ")
    user_program_decision = int(input("Escoja una opción: "))
    return user_program_decision


# Method to run different programs
def use_programs(user_program_decision):
    if user_program_decision == 1:
        CalendarIdea.start_program()
    elif user_program_decision == 2:
        MisteryProgram.start_program()
    elif user_program_decision == 3:
        PrintFigures.start_program()
    elif user_program_decision == 4:
        ListPairsAndOdds.start_program()
    elif user_program_decision == 5:
        PrintSquares.start_program()
    elif user_program_decision == 6:
        WordReverse.start_program()
    elif user_program_decision == 7:
        PrintTables.start_program()
    elif user_program_decision == 8:
        DeadBodyGame.start_program()
    elif user_program_decision == 9:
        BusStation.start_program()



