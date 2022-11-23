if __name__ == '__main__':
    total_grade = 0
    grade_counter = 0
    grade = int(input("Enter student grades or -1 to quit the program: "))
    while grade != -1:
        total_grade += grade

        grade = int(input("Enter student grades or -1 to quit the program: "))
        grade_counter += 1
    if grade_counter != 0:
        average = total_grade / grade_counter
        print("The total grades entered is: %d\nTotal grade is: %d\nAverage grade is: %d" %(grade_counter, total_grade, average))
    else:
        print("No grade!")