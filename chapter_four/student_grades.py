if __name__ == '__main__':


    total = 0
    count = 1
    while count <= 10:
        try:
            grade = int(input("Enter student grade: "))
            total += grade
            count += 1
        except ValueError:
            print()
            print("Invalid literal")
    average = total / grade
    print(count)
    print(total)
    print(average)
