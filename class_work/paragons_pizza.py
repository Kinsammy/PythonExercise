import math


def paragons(pizza_amount, current_balance, offender_fee):
    return math.ceil((pizza_amount - current_balance) / offender_fee)


def order_pizza():
    pizza_amount = int(input("Enter pizza amount: "))
    current_balance = int(input("Enter the amount your have at hand: "))
    offender_fee = int(input("Enter offender's fee: "))
    return math.ceil((pizza_amount - current_balance) / offender_fee)


if __name__ == '__main__':
    # print("The Total people we need if they are paying #100 is: ", paragons(12000, 4300, 100))
    # print("The Total people we need if they are paying #200 is: ", paragons(12000, 4300, 200))
    # print("The Total people we need if they are paying #500 is: ", paragons(12000, 4300, 500))
    # print("The Total people we need if they are paying #1000 is: ", paragons(12000, 4300, 1000))

    print("You need ", order_pizza(), "People")

