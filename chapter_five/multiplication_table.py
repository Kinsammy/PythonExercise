def multiplication(number):
    for count in range(13):
        print(f"{number} * {count} =", number * count)


if __name__ == '__main__':
    numbers = int(input("Enter a number: "))
    multiplication(numbers)
