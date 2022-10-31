def while_loop(numbers):
    total = 0
    count = 1
    while count < len(numbers):
        total += numbers[count]
        count += 1
    return total


def for_loop(numbers):
    total = 0
    for index in range(1, len(numbers)):
        total += numbers[index]
    return total


if __name__ == '__main__':
    user_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("The while loop total is: %d" % while_loop(user_input))
    print("The for loop total is: %d" % for_loop(user_input))
