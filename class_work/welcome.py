if __name__ == '__main__':
    print("\t\tWelcome\nSamuel To PYTHON CLASS!")
    first_number = int(input("Enter first number:\n"))
    second_number = int(input("Enter second number:\n"))
    total = first_number / second_number
    print("%d + %d = %d " % (first_number,second_number,total))
    if first_number > second_number:
        print("%d is greater than %d" % (first_number, second_number))

