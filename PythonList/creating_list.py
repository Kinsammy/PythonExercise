if __name__ == '__main__':
    # creating empty list and adding values to list
    a_list = []
    for number in range(1, 11):
        a_list += [number]
    print(a_list)

    # Accessing values by iteration
    for item in a_list:
        print(item)

    # Accessing list by index
    print("Subscript     Value")
    for index in range(len(a_list)):
        print("%5d %11d" % (index, a_list[index]))
