# create object of class Time
from PythonClasses.Time import Time

if __name__ == '__main__':

    time1 = Time()
    print("The attributes of time1 are: ")
    print("time1.hour:", time1.hour)
    print("time1.minute:", time1.minute)
    print("time1.second:", time1.second)

    print("\nCalling method printMillitary:", time1.printMilitary())
    print("\nCalling method printStandard:", time1.printStandard())
    print("\n\nChanging time1's hour attribute...")
    time1.hour = 25
    print("\nCalling method printMillitary afte alteration:", time1.printMilitary())