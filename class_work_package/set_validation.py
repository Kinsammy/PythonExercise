def set_validation():
    data_set = set()
    while True:
        try:
            for x in range(1, 6):
                user_input = int(input("Enter five(5) difference numbers between 2 and 90: "))
                if 2 <= user_input <= 90:
                    data_set.add(user_input)
                else:
                    raise OverflowError("Your input is not in the range")
        except ValueError as error:
            print("Invalid input, try agian")
        except OverflowError:
            print("Your input is not in the range, try again")
        else:
            return data_set


if __name__ == '__main__':
    print(set_validation())
