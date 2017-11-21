# 11/7/17
# Double Trouble: "Roll Dice" Add Two Values if same double
# By Efrain
import random
Dice1 = random.randrange(1, 7)
Dice2 = random.randrange(1, 7)
if Dice1 != Dice2:
    Sum = Dice1 + Dice2
    print("The Die Rolled {} and {}".format(Dice1, Dice2))
    print("The Sum Of The Die Is {}".format(Sum))
if Dice1 == Dice2:
    Double = Dice1 * Dice2
    print("The Die Rolled {} and {}".format(Dice1, Dice2))
    print("The Product Of The Die Is {}".format(Double))

