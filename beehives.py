from math import hypot

while True:
	d, N = input().split()
	d, N = float(d), int(N)
	if d==0.0: break
	H = [tuple(map(float, input().split())) for _ in range(N)]
	sour = sum(any(hypot(X-x,Y-y)<=d for X, Y in H if X!=x or Y!=y) for x, y in H)
	print(sour, "sour,", int(N)-sour, "sweet")