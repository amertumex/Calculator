first_number = float(input("Enter a number: "))
second_number = float(input("Enter a second number: "))
operation = input("Enter a symbol: ")

if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "/":
    if second_number == 0:
        print("Division by zero")
    else:
        print(first_number / second_number)
else:
    print("Invalid operation")
