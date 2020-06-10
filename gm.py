def gm(num, r) :
    for i in range(0, 10) :
        print(num * pow(r, i))

r = int(input("The common ratio of your GM is :"))
num = int(input("The first term of the GM is :"))
gm(num, r)