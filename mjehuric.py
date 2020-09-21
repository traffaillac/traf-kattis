P = [int(i) for i in input().split()]
while P != [1, 2, 3, 4, 5]:
	for i in range(4):
		if P[i] > P[i+1]:
			P[i], P[i+1] = P[i+1], P[i]
			print(*P)
