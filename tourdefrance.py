while input() != '0':
	F = [int(i) for i in input().split()]
	R = [int(i) for i in input().split()]
	D = [(f,r) for f in F for r in R]
	D.sort(key=lambda t: t[1]/t[0])
	print(round(max((D[i+1][1] * D[i][0]) / (D[i][1] * D[i+1][0]) for i in range(len(D) - 1)), 2))
