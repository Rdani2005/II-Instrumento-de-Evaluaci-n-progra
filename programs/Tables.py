and_table = [
    "A  B   Result",
    "0  0     0   ",
    "1  0     0   ",
    "0  1     0   ",
    "1  1     1   "
]

or_table = [
    "a  b   Result",
    "0  0      0  ",
    "1  0      1  ",
    "0  1      1  ",
    "1  1      1  "
]

not_table = [
    "a  ~a",
    "1   0 ",
    "0   1 "
]


def print_and():
    print("TABLA AND")
    for i in range(0, len(and_table)):
        print(and_table[i])


def print_or():
    print("TABLA OR")
    for i in range(0, len(or_table)):
        print(or_table[i])


def print_not():
    print("TABLA NOT")
    for i in range(0, len(not_table)):
        print(not_table[i])


# case
switch_table = {
    1: print_and,
    2: print_or,
    3: print_not
}


def start_program():
    print("Bienvenido al Tablas: ")
    should_continue = True

    while should_continue:
        # Ask the user the table that want to see
        num = int(input("Cual tabla desea ver (1. And 2. Or 3. Not): "))
        switch_table.get(num, "Error")()
        # Should we continue the program?
        user_decision = int(input("Desea ver otra tabla? (1. si, 2. no): "))
        if user_decision == 2:
            should_continue = False
            print("Le deseamos exitos en sus labores")
        elif user_decision == 1:
            print("Perfecto, volvamos al principio")
        else:
            print("Opción invalida, por eso seguiremos con el programa")


