import random


def GuessGame(n):
    dice = random.randint(1, 6)
    print(dice)
    if(n == dice):
        print("won")

    else:
        print("lost")


GuessGame(2)
