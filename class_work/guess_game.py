import random
if __name__ == '__main__':
    # random.seed(104)
    number = random.randint(7, 10)
    count = 0
    while count <= 3:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print("You got it right!")
            break
        count += 1
