for _ in range(int(input())):
	g, m = 0, 0
	for i in range(int(input())):
		a, b, c = map(int, input().split())
		R = b / 2 / a
		T = -a*R*R + b*R + c
		if T > m:
			g, m = i+1, T
	print(g)
