def display(product_num, quantity, unit, ):
    print("%10s%20s%20s%20s" % ("Product Name", "Quantity", "Unit Price", "Total"))
    for element in range(product_num):
        print("%10d%20d%20.f%20.2f" % (
            product_num[element], quantity[element], unit[element], (quantity[element] * unit[element])))
    print("%50s%20.2f" % ("Grand Total", product_grand_total(quantity, unit)))


def product_grand_total(quantity, price):
    total = quantity * price
    grand_total = 0
    for index in range(quantity):
        grand_total += total
    return grand_total


if __name__ == '__main__':
    product_list = []
    quantity_list = []
    unit_price_list = []

    while True:
        product_number = int(input("Enter product number: "))
        product_list.append(product_number)
        product_quantity = int(input("Enter product quantity: "))
        quantity_list.append(product_quantity)
        unit_price = float(input("Enter unit price: "))
        unit_price_list.append(unit_price)
        option = input("Any other sale? 'yes' or 'no': ").lower()
        if option != "yes":
            display(product_list, quantity_list, unit_price_list)
            break
