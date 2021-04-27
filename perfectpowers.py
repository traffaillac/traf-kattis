from math import exp, log

while True:
	x = int(input())
	if x == 0:
		break
	*_, p = (p for p in range(1, 32) if (x>0 or p%2==1) and round(exp(log(abs(x))/p))**p==abs(x))
	print(p)
