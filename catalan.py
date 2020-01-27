from math import factorial

q = int(input())
for i in range(q):
	x = int(input())
	print(factorial(2*x) // (factorial(x+1) * factorial(x)))
