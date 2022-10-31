if __name__ == '__main__':
    print("The list Comprehension process:")
    numbers = [1, 2, 3, 4, 5]
    square = [index ** 2 for index in numbers]
    print(square)

    print("The main list process:")
    square = []
    for index in numbers:
        square.append(index**2)
    print(square)
