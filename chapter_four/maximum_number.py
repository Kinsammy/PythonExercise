def maximum_value(x, y, z):
    maximum = x
    if y > maximum:
        maximum = y
    if z > maximum:
        maximum = z

    return maximum


if __name__ == '__main__':
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    print("the maximum nuber is: ", maximum_value(a, b, c))
