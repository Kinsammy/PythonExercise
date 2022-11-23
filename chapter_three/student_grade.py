if __name__ == '__main__':
    total = 0
    grade_counter = 1

    while grade_counter <= 10:
        grade = int(input("Enter student grades: "))
        total += grade
        grade_counter += 1

    average = total / 10
    print("Class average is", average)
