import random

while 1 :
    value = input("Do you want to roll the dice : ")
    if value != "no" :
        print(random.randrange(1, 6, 1))
    else :
        break