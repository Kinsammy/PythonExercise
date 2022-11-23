def calculation():
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    operator = input("Enter operator sign: ")
    if operator == "+":
        print("Addition Calculation")
        print(f"{first_number} {operator} {second_number} =", first_number + second_number)
    elif operator == "-":
        print("Subtraction Calculation")
        print(f"{first_number} {operator} {second_number} =", first_number - second_number)
    elif operator == "*":
        print("Multiplication Calculation")
        print(f"{first_number} {operator} {second_number} =", first_number * second_number)
    elif operator == "**":
        print("Exponential Calculation")
        print(f"{first_number} {operator} {second_number} =", first_number ** second_number)
    elif operator == "/" or operator == "//":
        print("Division Calculation")
        operator = input("Enter operator / for float division or // integer division: ")
        if operator == "/":
            print("Float Division calculation")
            print(f"{first_number} {operator} {second_number} =", first_number / second_number)
        elif operator == "//":
            print("Integer Division")
            print(f"{first_number} {operator} {second_number} =", first_number // second_number)
    elif operator == "%":
        print("Modulus or Reminder")
        print(f"{first_number} {operator} {second_number} =", first_number % second_number)

    print("Thanks for using Sammy Calculator")


if __name__ == '__main__':
    calculation()
