import random

if __name__ == '__main__':

    for i in range(1, 21):
        print("%10d" % (random.randrange(1, 7)), end=' ')
        if i % 5 == 0:
            print()
