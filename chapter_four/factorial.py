if __name__ == '__main__':
    number = int(input("Enter a number for Factorial: "))
    factorial = 1

    for counter in range(1, number + 1):
        factorial *= counter

    print("The factorial of %d is %d" % (number, factorial))
