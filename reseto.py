N, K = map(int, input().split())
P = [True] * (N+1)
p = 2
k = 0
while True:
	while not P[p]:
		p += 1
	for i in range(p, N+1, p):
		if P[i]:
			P[i] = False
			k += 1
			if k==K:
				print(i)
				exit()
