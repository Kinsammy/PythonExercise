class Time:
    #  belowis constructor
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0

    def printMilitary(self):
        print("%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second))

    def printStandard(self):
        standartTime = ""
        if self.hour == 0 or self.hour == 12:
            standartTime += "12:"
        else:
            standartTime += "%d" % (self.hour % 12)
        standartTime += "%.2d: %.2d" % (self.minute, self.second)
        if self.hour < 12:
            standartTime += " AM"
        else:
            standartTime += " PM"
        print(standartTime)


