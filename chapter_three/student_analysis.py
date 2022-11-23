if __name__ == '__main__':
    passes = 0
    failure = 0
    student_counter = 1
    while student_counter <= 10:
        result = int(input("Enter number 1 for pass and number 2 for fail: "))
        if result == 1:
            passes = passes + 1

        else:
            failure = failure + 1

        student_counter = student_counter + 1
    print("Passed: ", passes)
    print("Failed: ", failure)

    if passes > 8:
        print("You have a bonus!")
