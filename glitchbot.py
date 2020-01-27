from sys import exit

target = tuple(int(i) for i in input().split())
orig = [input() for _ in range(int(input()))]

def run(inst):
	x, y, dx, dy = 0, 0, 0, 1
	for i in inst:
		if i == 'Forward':
			x += dx
			y += dy
		elif i == 'Left':
			dx, dy = -dy, dx
		elif i == 'Right':
			dx, dy = dy, -dx
	return x, y

for i, o in enumerate(orig):
	for mod in ('Forward', 'Left', 'Right'):
		orig[i] = mod
		if run(orig) == target:
			print(i+1, mod)
			exit()
	orig[i] = o
