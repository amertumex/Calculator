def calculator(first_number, second_number, operation):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        if second_number == 0:
            return "Division by zero"
        else:
            return first_number / second_number
    else:
        return "Invalid operation"


first_number = float(input("Enter a number: "))
second_number = float(input("Enter a second number: "))
operation = input("Enter a symbol: ")


print(calculator(first_number, second_number, operation))