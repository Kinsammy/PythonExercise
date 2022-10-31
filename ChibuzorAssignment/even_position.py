def position(user_input):
    new = []
    for index in range(len(user_input)):
        new.append(user_input[index])
        if index % 2 == 0:
            print(user_input[index])


if __name__ == '__main__':
    input_number = [1, 2, 3, 4, 5, 6, 7]
    print(position(input_number))
