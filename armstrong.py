upto = int(input("Print upto : "))
for i in range(1, upto) :
    order = len(str(i))
    sum = 0
    j = i
    while i > 0 :
        a = i % 10
        sum = sum + a ** order
        i = i // 10
    if j == sum :
        print(sum)