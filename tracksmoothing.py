from math import hypot, pi
for _ in range(int(input())):
	r, n = map(int, input().split())
	X, Y = [], []
	for _ in range(n):
		x, y = map(int, input().split())
		X.append(x)
		Y.append(y)
	l = 0
	for i in range(n):
		l += hypot(X[i-1]-X[i], Y[i-1]-Y[i])
	print((l-2*pi*r)/l if l>=2*pi*r else "Not possible")