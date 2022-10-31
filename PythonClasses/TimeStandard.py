class Time:
    """"Class Timewith accessor methods"""

    def __init__(self):
        self._hour = 0
        self._minute = 0
        self._second = 0

    def setTime(self, hour, minute, second):
        self.setHour(hour)
        self.setMinute(minute)
        self.setSecond(second)

    def setHour(self, hour):
        if 0 <= hour < 24:
            self._hour = hour
        else:
            raise ValueError("Invalid hour value: %d" % hour)

    def setMinute(self, minute):
        if 0 <= minute < 60:
            self._minute = minute
        else:
            raise ValueError("Invalid minute value: %d" % minute)

    def setSecond(self, second):
        if 0 <= second < 60:
            self._second = second
        else:
            raise ValueError("Invalid second value: %d" % second)

    def getHour(self):
        return self._hour

    def getMinute(self):
        return self._minute

    def getSecond(self):
        return self._second

    def printMilitary(self):

        print("%.2d:%.2d:%.2d" % (self._hour, self._minute, self._second))

    def printStandard(self):
        standartTime = ""
        if self._hour == 0 or self._hour == 12:
            standartTime += "12:"
        else:
            standartTime += "%d" % (self._hour % 12)
        standartTime += "%.2d: %.2d" % (self._minute, self._second)
        if self._hour < 12:
            standartTime += " AM"
        else:
            standartTime += " PM"
        print(standartTime)
