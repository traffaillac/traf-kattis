from sys import stdin
from math import acos, hypot, pi, sin
for l in stdin:
	r, x, y = map(float, l.split())
	if hypot(x, y)>r:
		print("miss")
	else:
		a = acos(hypot(x, y) / r) * 2
		A = r*r/2*(a-sin(a))
		print(pi*r*r-A, A)
