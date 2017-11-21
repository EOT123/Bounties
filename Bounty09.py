# 10/30/17
# Life potions Random potion amount 0-100 / E=Decrease Potions
import random
potion = (random.randint(0, 100))
print('You Have {} Potions'.format(potion))
while True:
    print("")
    action = input('Enter e To Use A Potion : ')
    if action == "e":
        potion = potion - 1
        print(potion)
    if potion == 0:
        potion = potion + 1
        print("You Are Out Of Potions!")
        print("Enter n To Exit")
    if action == "n":
        break
# Done
