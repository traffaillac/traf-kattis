# Golfed afterwards though not kept ;)
from math import asin, atan2, hypot, pi
for _ in range(int(input())):
	n, d = map(int, input().split())
	I, J = [], []
	for _ in range(n):
		x, y = map(int, input().split())
		if hypot(x, y) <= d: continue
		a = atan2(y, x)
		da = asin(d / hypot(x, y))
		I.append(((a-da)%(2*pi), (a+da)%(2*pi)))
		J.append(((-a-da)%(2*pi), (-a+da)%(2*pi)))
	I.sort()
	J.sort()
	i = 0
	while I:
		i += 1
		a = I.pop()[0]
		while I and not I[-1][0]<=I[-1][1]<a:
			I.pop()
	j = 0
	while J:
		j += 1
		a = J.pop()[0]
		while J and not J[-1][0]<=J[-1][1]<a:
			J.pop()
	print(min(i, j))