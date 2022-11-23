from chapter_four.chance_game import ChanceGame, rollDice

# class ChanceGameApp:
if __name__ == '__main__':
    player = ChanceGame()

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    player.__set_data__(name, age)
    print("Player name is %s\nAnd player age is:%d" % (name, age))
    play = int(input("Press 1 to play the game:"))
    sum_of_dice = rollDice()
    my_point = 0

    if sum_of_dice == 7 or sum_of_dice == 11:
        gameStatus = "WON"
    elif sum_of_dice == 2 or sum_of_dice == 3 or sum_of_dice == 12:
        gameStatus = "LOST"
    else:
        gameStatus = "CONTINUE"
        my_point = sum_of_dice
        print("Point is", my_point)

    while gameStatus == "CONTINUE":
        play = int(input("Press 1 to play the game:"))
        sum_of_dice = rollDice()
        if sum_of_dice == my_point:
            gameStatus = "WON"
        elif sum_of_dice == 7:
            gameStatus = "LOST"

    if gameStatus == "WON":
        print("%s WINS!" % name)
    else:
        print("%s LOSES!" % name)
