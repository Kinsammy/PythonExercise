from PythonClasses.TimeStandard import Time

if __name__ == '__main__':
    time1 = Time()
    print("The initial military time is", time1.printMilitary())
    print("\nThe initial standard time is", time1.printStandard())

    time1.setTime(13, 27, 6)
    print("\n\nMilitary time after setTime is",
          time1.printMilitary())
    print("\nStandard time after setTime is", time1.printStandard())
