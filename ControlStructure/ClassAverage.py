if __name__ == '__main__':

    total = 0
    grade_counter = 1
    while grade_counter <= 10:
        grade = int(input(f"Enter grade {grade_counter}: "))
        total += grade
        grade_counter += 1

    average = total / 10
    print("The Total grade is: %d\nThe Average:  %.2f" % (total, average))
