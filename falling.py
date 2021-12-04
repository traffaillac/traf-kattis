from math import sqrt

D = int(input())
for a in range(1, int(sqrt(D)) + 1):
	if D % a == 0:
		b = D // a
		if a & 1 == b & 1:
			print((b - a) // 2, (b + a) // 2)
			break
else:
	print('impossible')
