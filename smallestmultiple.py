from functools import reduce
from math import gcd
from sys import stdin

for line in stdin:
	N = list(map(int, line.split()))
	d = gcd(*N)
	print(reduce(lambda x,y: x*y, N, 1) // d)
