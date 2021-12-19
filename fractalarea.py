from math import pi

for _ in range(int(input())):
	r, n = map(int, input().split())
	area = pi * r * r
	inc = area
	for _ in range(1, n):
		area += inc
		inc *= 3 / 4
	print(area)
