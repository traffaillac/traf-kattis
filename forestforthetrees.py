from math import gcd
from sys import exit

xb, yb = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
d = gcd(xb, yb)
if d == 1:
	print('Yes')
	exit()
dx = xb // d
dy = yb // d
if not x1 <= dx <= x2 or not y1 <= dy <= y2:
	print('No')
	print(dx, dy)
	exit()
i = min(x2 // dx, y2 // dy) + 1
if i * dx < xb:
	print('No')
	print(i * dx, i * dy)
else:
	print('Yes')
