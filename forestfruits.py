from heapq import heappush, heappop
from sys import stdin

def main():
	V, E, C, K, M = map(int, next(stdin).split())
	rem = min(K, M)
	if rem > C:
		return -1
	graph = [{} for _ in range(V)]
	for _ in range(E):
		u, v, w = map(int, next(stdin).split())
		graph[u-1][v-1] = w
		graph[v-1][u-1] = w
	fruits = set(int(c)-1 for c in next(stdin).split())
	heap = [(0, 0)]
	dist = [20_000_000_000] * V
	dist[0] = 0
	while heap:
		d, u = heappop(heap)
		if d > dist[u]:
			continue
		if u in fruits:
			rem -= 1
			if rem == 0:
				return d * 2
		for v, w in graph[u].items():
			if dist[v] > d+w:
				dist[v] = d+w
				heappush(heap, (d+w, v))
	return -1

print(main())
