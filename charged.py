from bisect import *
from math import *

n, m, q = map(int, input().split())
P = [tuple(map(int,(input()+'1').split())) for _ in range(q)]
T = [-1/pi,-1/pi**2,-1/pi**3,1/pi**3,1/pi**2,1/pi]
for y in range(1, n+1):
	for x in range(1, m+1):
		if (x, y, -1) in P:
			print('-', end='')
		elif (x, y, 1) in P:
			print('+', end='')
		else:
			print("%Xx.oO0"[bisect(T, sum(q/hypot(X-x,Y-y) for X, Y, q in P))], end='')
	print()
