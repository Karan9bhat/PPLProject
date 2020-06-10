import math

arr = []

def ore(num) :
	for div in range(1, (num + 1)) :
		if num % div == 0 :
			arr.append(div)
	Sum = 0
	length = len(arr)
	for i in range(0, length) :
		Sum = Sum + (num / arr[i])
	Sum = Sum / num
	x = length / Sum
	arr.clear()
	if x.is_integer():
		return True
	else :
		return False

count = 0
for num in range(1, 100000) :
	#print(1)
	if ore(num) :
		print(num)
		count += 1
		if count > 9 :
			break
