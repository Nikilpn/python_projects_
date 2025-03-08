import os
def calculator():
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiple(a, b):
        return a * b

    def divide(a, b):
        return a / b

    operations_dict = {

        "+": add,
        "-": subtract,
        "*": multiple,
        "/": divide
    }
    number1 = float(input("enter first number :"))


    for symbol in operations_dict:
        print(symbol)
    continue_flag = True
    while continue_flag:
        op_symbol = input("enter an operation")
        number2 = float(input("enter the next number :"))
        calc_function = operations_dict[op_symbol]
        output = calc_function(number1, number2)
        print(f"{number1} {op_symbol} {number2}= {output}")

        should_continue = input("Type 'y' to continue operation,'x' to exit"
                                " and 'n' to start a new calculator ").lower()
        if should_continue == 'y':
            number1 = output
            continue_flag = True
        elif should_continue == 'n':
            os.system('cls')
            calculator()

        else :
            print('Bye')
            continue_flag = False




calculator()