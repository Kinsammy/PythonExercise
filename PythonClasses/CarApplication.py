from PythonClasses.Car import Car
if __name__ == '__main__':
    first = Car("Camary 5044", "2022",  700000.0)
    print("Car initial detail:\nModel: %s\nYear: %s\nPrice: %.2f\nDiscount: %.2f" % (first.getModel(), first.getYear(), first.getPrice(), first.getDiscount1()))
    first.setModel("Lexus E50")
    first.setYear("2022")
    first.setPrice(859432.56)

    print("Car initial detail:\nModel: %s\nYear: %s\nPrice: %.2f\nDiscount: %.2f" % (first.getModel(), first.getYear(), first.getPrice(), first.getDiscount2()))