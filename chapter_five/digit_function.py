def get_digit(number, position):
    return number // (10 ** position) % 10


if __name__ == '__main__':
    print(get_digit(1500, 3))
