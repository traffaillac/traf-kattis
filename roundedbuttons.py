from math import hypot

for _ in range(int(input())):
	x, y, w, h, r, m, *clicks = map(float, input().split())
	for i in range(int(m)):
		X, Y = clicks[i * 2], clicks[i * 2 + 1]
		inside = (
			x <= X <= x+w and y+r <= Y <= y+h-r or
			x+r <= X <= x+w-r and y <= Y <= y+h or
			hypot(x+r-X, y+r-Y) <= r or
			hypot(x+w-r-X, y+r-Y) <= r or
			hypot(x+r-X, y+h-r-Y) <= r or
			hypot(x+w-r-X, y+h-r-Y) <= r)
		print('inside' if inside else 'outside')
	print()
