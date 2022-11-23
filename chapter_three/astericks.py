if __name__ == '__main__':

    for x in range(1, 11):
        for i in range(1, x):
            print("*", end=' ')
        print()
    print()

    for x in range(11, 0, -1):
        for i in range(1, x):
            print("*", end=' ')
        print()
    print()

    # for x in range(11, 0, -1):
    #     for i in range(x, 0, -1):
    #         print("*", end=' ')
    #     print()
    # print()
