if __name__ == '__main__':

    principal = 1000.0
    rate = 0.05
    amount = 0
    print("Year %21s" % "amount on deposit")
    for year in range(1, 11):
        # amount = invest * (1 + math.pow(rate, year))
        amount = principal * (1.0 + rate) ** year
        print("%4d%21.2f" % (year, amount))
