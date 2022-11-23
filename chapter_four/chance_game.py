import random


def rollDice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    sum_dice = die1 + die2
    print("Player rolled %d + %d = %d" % (die1, die2, sum_dice))
    return sum_dice


class ChanceGame:

    def __set_data__(self, name, age):
        self.name = name
        if age >= 18:
            self.age = age
        else:
            print("You are young!")

    def __get_data__(self):
        return self.name + self.age
