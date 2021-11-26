# Data import from AskFiles
import AskFiles


# Copyright
__author__ = "Danny Sequeira"
__copyright__ = "Copyright (C) 2021 Danny Sequeira"


def run_different_programs():
    should_continue = True

    # Begging the program
    while should_continue:
        user_decision_program = AskFiles.welcome()
        AskFiles.use_programs(user_decision_program)
        # Ask if we continue this or stop it
        user_decision = int(input("Volviendo al programa del instrumento, Desea escoger otro programa? (1. si, 2. no): "))
        if user_decision == 2:
            should_continue = False
            print("Le deseamos exitos en sus labores")
        elif user_decision == 1:
            print("Perfecto, volvamos al principio")
        else:
            print("Opción invalida, por eso seguiremos con el programa")


# Main method
if __name__ == '__main__':
    run_different_programs()
