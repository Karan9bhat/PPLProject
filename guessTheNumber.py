import random

i = 1
answer = random.randrange(1, 200, 1)
while i :
    guess = int(input("Your guess is : "))
    if guess < answer :
        print("Your guess is less than the number")
    elif guess > answer :
        print("Your guess is greater than the number")
    elif guess == answer :
        print("This is the correct number")
        i = 0
