def reverse_list(user_input):
    new_list = []
    for index in user_input:
        new_list.insert(0, index)
    return new_list


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7]
    print(reverse_list(numbers))
