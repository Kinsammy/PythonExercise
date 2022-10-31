"""A college offers a course that prepares students for the state licensing exam for real estate
brokers. Last year, several of the students who completed this course took the licensing
examination. Naturally, the college wants to know how well its students did on the exam. You
have been asked to write a program to summarize the results. You have been given a list of
these 10 students. Next to each name is written a 1 if the student passed the exam and a 2 if
the student failed."""

if __name__ == '__main__':

    passes = 0
    failures = 0
    student_counter = 1
    while student_counter <= 10:
        result = int(input("Enter 1 for passes and 2 for failure: "))
        if result == 1:
            passes += 1
        else:
            failures += 1
        student_counter += 1

    print("Total student that passes are: %d" % passes)
    print("Total student that falure are: %d" % failures)

    if passes > 8:
        print("Raise tuition.")