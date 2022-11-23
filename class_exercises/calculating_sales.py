def product(number, qty):
    return number + qty


# def product_price(number):
#     total_sold = 0
#     product_sold = 0
#     match number:
#         case 1:
#             product_sold = quantity * 2.98
#         case 2:
#             product_sold = quantity * 4.50
#         case 3:
#             product_sold = quantity * 9.98
#         case 4:
#             product_sold = quantity * 4.49
#         case 5:
#             product_sold = quantity * 6.87
#     return total_sold + product_sold


if __name__ == '__main__':
    total = 0
    price = 0
    product_counter = 0

    while True:
        product_number = int(input("Enter product number: "))
        quantity = float(input("Enter quantity sold : "))
        product(product_number, quantity)
        match product_number:
            case 1:
                price = quantity * 2.98
            case 2:
                price = quantity * 4.50
            case 3:
                price = quantity * 9.98
            case 4:
                price = quantity * 4.49
            case 5:
                price = quantity * 6.87
        total += price
        product_counter += 1
        option = input("Any Other product? Enter 'yes' or 'no'\n").lower()
        if option != "yes":
            if product_counter != 0:
                print("The Total products Sold is: %.2f" % total)
            break



