import math

def sumOfDiv(x) :
    sum = 1
    for i in range(2, int(math.sqrt(x))) :
        if x % i == 0 :
            sum = sum + i
            if i != x % i :
            	sum = sum + x/i
    return sum

def isAmicable(a, b) :
    if sumOfDiv(a) == b and sumOfDiv(b) == a :
        return True
    else :
        return False

count = 1
for m in range(1, 100000) :
    for n in range(2, m) :
        if isAmicable(m, n) :
            print("The pair is :", m, n)
            count = count + 1
            if count == 10 :
                break
