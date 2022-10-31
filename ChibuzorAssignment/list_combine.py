def combine(first_list, second_list):
    new_list = []
    for index , count in zip(first_list, second_list):
        new_list.append(index)
        new_list.append(count)
    return new_list


if __name__ == '__main__':
    letter_list = ['a', 'b', 'c']
    numeric_list = [1, 2, 3]
    print(print(combine(letter_list, numeric_list)))