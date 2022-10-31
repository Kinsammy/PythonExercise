def max_number(user_input):
    max_va = user_input[0]
    for index in user_input:
        if index > max_va:
            max_va = index
    # return max(user_input)
    return max_va


def min_number(user_input):
    min_va = user_input[0]
    for index in user_input:
        if index < min_va:
            max_va = index
    # return max(user_input)
    return min_va
    # return min(user_input)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    print("The maximum is: %d" % max_number(numbers))
    print("The minimum is: %d" % min_number(numbers))