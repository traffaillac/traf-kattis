from math import pi, sin, cos
for _ in range(int(input())):
	x, y, a = 0, 0, 0
	for _ in range(int(input())):
		da, d = map(float, input().split())
		a = (a+da*pi/180)%(pi*2)
		x -= d*sin(a)
		y += d*cos(a)
	print(x, y)