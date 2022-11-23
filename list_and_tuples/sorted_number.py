def sorted_list(str_list, in_list):
    list_ = []
    for word in in_list:
        list_.append(int(word))
    return sorted(str_list) + sorted(list_)


if __name__ == '__main__':
    str_list = input("Enter a word or sentences: ")
    int_list = input("Enter some integers: ")
    print(sorted_list(str_list, int_list))

