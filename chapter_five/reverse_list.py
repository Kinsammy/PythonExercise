def reverse_number(user_list):
    reverse_list = [len(user_list)]
    backward_counter = user_list - 1
    forward_counter = 0
    while backward_counter != -1:
        reverse_list[forward_counter] = user_list[backward_counter]
        forward_counter += 1
        backward_counter -= 1
        return reverse_list


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    number_collection = reverse_number()
    print(number_collection)
