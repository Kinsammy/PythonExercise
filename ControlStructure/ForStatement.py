"""Use for statement to print number from 1 to 10 and from 10 to 1"""

if __name__ == '__main__':
    for counter in range(1, 11):
        print(counter, end=' ')
    print()
    for count in range(10, 0, -1):
        print(count, end=' ')
