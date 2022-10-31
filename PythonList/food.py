if __name__ == '__main__':
    food = ["rice", "beans"]
    food.append("broccoli")
    print("For appending broccoli\n", food)
    food.extend(["bread", "pizza"])
    print("using extend method\n", food)
    print("Printing first two element\n",food[0:2])


