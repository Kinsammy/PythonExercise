def running_total(user_input):
    total = 0
    for index in user_input:
        total += index
    return total


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    print("Using function: %d" % running_total(numbers))
    print("Using built-in: %d" % sum([1, 2, 3, 4, 5]))
