from itertools import product

for _ in range(int(input())):
	S, H = map(int, input().split())
	C = {tuple(map(int, input().split())) for _ in range(H)}
	for X, Y in product(range(1, S), repeat=2):
		if (X, Y) in C: continue
		r2 = max((x-X)**2+(y-Y)**2 for x, y in C)
		if r2<=min(X,S-X,Y,S-Y)**2:
			print(X, Y)
			break
	else:
		print("poodle")