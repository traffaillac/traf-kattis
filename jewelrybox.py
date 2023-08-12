for _ in range(int(input())):
	X, Y = map(int, input().split())
	h = (X+Y-(X*X+Y*Y-X*Y)**.5)/6
	print((X-2*h)*(Y-2*h)*h)