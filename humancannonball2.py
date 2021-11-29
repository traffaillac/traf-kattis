from math import cos, sin, pi

for _ in range(int(input())):
	v0, th, x1, h1, h2 = map(float, input().split())
	t = x1 / (v0 * cos(th * pi / 180))
	y = v0 * t * sin(th * pi / 180) - 0.5 * 9.81 * t * t
	print('Safe' if h1 + 1 <= y <= h2 - 1 else 'Not Safe')
