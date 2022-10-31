def convert_list(numbers):
    new_list = list(numbers)
    return new_list


if __name__ == '__main__':
    # user_input = input("Enter digits of integer to convert to list: ")
    user_input = (1, 2, 3, 4,)
    print("The new list is: ", convert_list(user_input))
