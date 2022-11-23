if __name__ == '__main__':
    colors = {'red', 'blue', 'red', 'black', 'yellow', 'white'}
    print(colors)

    print("The length is: %d" % len(colors))
    print("\nExistence of color")
    var = 'red' in colors
    print(var)
    print("\nIteraing through a sets")
    for color in colors:
        print(color)
