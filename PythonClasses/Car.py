class Car:

    def __init__(self, model, year, price):
        self._model = model
        self._year = year
        self._price = price

    def setModel(self, model):
        self._model = model

    def getModel(self):
        return self._model

    def setYear(self, year):
        self._year = year

    def getYear(self):
        return self._year

    def setPrice(self, price):
        self._price = price

    def getPrice(self):
        return self._price

    def getDiscount1(self):
        return self.getPrice() // 100 * 5

    def getDiscount2(self):
        return self.getPrice() // 100 * 7
