from heapq import heappush, heappop

# edge cases:
# - depending on desired remaining volume, the best road may vary
# - overfilling at start to account for higher prices later
# - requiring to fill the tank entirely at some point
N, M = map(int, input().split())
prices = [int(p) for p in input().split()]
nodes = [[] for n in range(N)]
for m in range(M):
	u, v, d = map(int, input().split())
	nodes[u].append((v, d))
	nodes[v].append((u, d))

Q = int(input())
for q in range(Q):
	C, S, E = map(int, input().split())
	pricemin = [[10_000_000] * (C + 1) for n in range(N)]
	pricemin[S][0] = 0
	heap = [(0, S, 0)]
	while heap:
		p, n, g = heappop(heap)
		if pricemin[n][g] >= p:
			if n == E:
				break
			if g < C and pricemin[n][g + 1] > p + prices[n]:
				pricemin[n][g + 1] = p + prices[n]
				heappush(heap, (p + prices[n], n, g + 1))
			for m, d in nodes[n]:
				if d <= g and pricemin[m][g - d] > p:
					pricemin[m][g - d] = p
					heappush(heap, (p, m, g - d))
	print(pricemin[E][0] if pricemin[E][0] < 10_000_000 else 'impossible')
