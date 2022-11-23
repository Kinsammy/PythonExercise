if __name__ == '__main__':
    for row in range(0, 10):
        for column in range(1, 10):
            new_list = row + column
            if new_list > 9:
                new_list -= 9
            print(new_list, end=" ")
        print()


