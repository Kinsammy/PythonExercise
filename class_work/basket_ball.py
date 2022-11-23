if __name__ == '__main__':
    i = 0
    while i < 10:
        name = str(input("Enter your name: "))
        if name == "new_native":
            print("you are welcome", name)
            break
        elif name == "old_native":
            print("You keep moving", name)
            break
        else:
            print("You are Senior!", name)
            break
    i += 1
