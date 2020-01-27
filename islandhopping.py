from heapq import heappop, heappush
from math import hypot

def dist(a, b):
	return hypot(a[0] - b[0], a[1] - b[1])

N = int(input())
for n in range(N):
	M = int(input())
	islands = [tuple(map(float, input().split())) for m in range(M)]
	visited = [False] * M
	distmin = [10000.0] * M
	heap = [(0.0, 0)]
	length = 0.0
	while len(heap) > 0:
		d, i = heappop(heap)
		if visited[i]:
			continue
		visited[i] = True
		length += d
		for j in range(M):
			if visited[j]:
				continue
			d = dist(islands[i], islands[j])
			if d < distmin[j]:
				distmin[j] = d
				heappush(heap, (d, j))
	print(length)
