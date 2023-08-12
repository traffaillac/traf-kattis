for _ in range(int(input())):
	p = int(input())
	N = [100000] * 10001
	N[0] = 0
	coins = [int(input()) for _ in range(int(input()))]
	coins.sort(reverse=True)
	for c in coins:
		for i in range(10000 - c, -1, -1):
			if N[i]<100000 and N[i]+1<N[i+c]:
				N[i+c] = N[i]+1
	i = next(i for i in range(p, 10001) if N[i]<100000)
	print(i, N[i])
