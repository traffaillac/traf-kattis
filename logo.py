from math import *

for _ in range(int(input())):
	a, x, y = 0, 0, 0
	for _ in range(int(input())):
		c, u = input().split()
		u = float(u)
		if c=="fd":
			x += u*cos(a)
			y += u*sin(a)
		elif c=="lt":
			a += u*pi/180
		elif c=="rt":
			a -= u*pi/180
		elif c=="bk":
			x -= u*cos(a)
			y -= u*sin(a)
	print(round(hypot(x, y)))