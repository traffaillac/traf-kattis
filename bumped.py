from heapq import heappush, heappop

# edge cases:
# - S == T
# - flights to not influence path thus heap does not end on T
# - flights ordered such that in place update would sum them
# - shortest path with flight is different than on road
N, M, F, S, T = map(int, input().split())
nodes = [[] for n in range(N)]
for m in range(M):
	i, j, c = map(int, input().split())
	nodes[i].append((j, c))
	nodes[j].append((i, c))

total = [2_500_000_000] * N
heap = [(0, S)]
flew = False
while heap:
	t, n = heappop(heap)
	if total[n] > t:
		total[n] = t
		if n == T:
			if flew:
				break
			flew = True
			heap.clear()
			for f in range(F):
				u, v = map(int, input().split())
				if total[v] > total[u]:
					heappush(heap, (total[u], v))
			continue
		for m, c in nodes[n]:
			if total[m] > t + c:
				heappush(heap, (t + c, m))
print(total[T])
