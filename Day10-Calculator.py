from Day10_1_art import logo
from replit import clear


def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    return first / second


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    first_num = float(input("What's the first number?: "))
    for op in operations:
        print(op)

    calculate = True

    while calculate:
        operation_symbol = input("Pick an operation: ")
        second_num = float(input("what's the next number?: "))

        function = operations[operation_symbol]
        answer = function(first_num, second_num)
        print(f"{first_num} {operation_symbol} {second_num} = {answer}")
        again = input(f"Type 'y' to continue calculating with {answer}, "
                      f"or type 'n' to start a new calculation: ")
        if again == "y":
            first_num = answer
            clear()
        else:
            calculate = False
            calculator()


calculator()