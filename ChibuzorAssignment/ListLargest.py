def largest(user_input):
    largest_value = user_input[0]
    for index in user_input:
        if index > largest_value:
            largest_value = index
    return largest_value


if __name__ == '__main__':
    numbers = [1, 2, 7, 3, 4, 5]
    print("The largest number is: %d" % largest(numbers))
