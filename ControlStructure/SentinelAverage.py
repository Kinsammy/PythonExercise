"""Develop a class-averaging program that processes an arbitrary number of grades each time
the program is executed."""

if __name__ == '__main__':
    total = 0
    grade_counter = 0

    grade = int(input(f"Enter grade: or -1 to guit the process: "))
    while grade != -1:
        total += grade
        grade_counter += 1

        grade = int(input(f"Enter grade{grade_counter} or -1 to guit the process: "))

    if grade_counter != 0:
        average = float(total / grade_counter)
        print("The Total grade is: %d\nThe Average:  %.2f" % (total, average))
    else:
        print("No grades")
