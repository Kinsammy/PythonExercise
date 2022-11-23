def sorting_algorithm(user_list):
    for index in range(len(user_list)):
        for count in range(index, len(user_list)):
            if user_list[count] < user_list[index]:
                temp = user_list[count]
                user_list[count] = user_list[index]
                user_list[index] = temp
    return user_list


if __name__ == '__main__':
    numbers = [1, 2, 3, 7, 8, 6, 4]
    print(sorting_algorithm(numbers))
