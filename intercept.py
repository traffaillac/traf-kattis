from heapq import heappush, heappop

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
	u, v, w = map(int, input().split())
	graph[u].append((v, w))
s, t = map(int, input().split())

dist = [None] * N # None if not explored (i.e. in heap), int otherwise
prev = [[] for _ in range(N)] # empty if not visited, will be the graph for second BFS
heap = [(0, s, -1)]
dist[s] = 0
while heap:
	W, u, parent = heappop(heap)
	if W > dist[u]: continue
	if not prev[u]:
		for v, w in graph[u]:
			if dist[v] is None or W+w <= dist[v]:
				dist[v] = W+w
				heappush(heap, (W+w, v, u))
	if parent >= 0:
		prev[u].append(parent)

heap = [(-dist[t], t)]
explored = [False] * N
explored[t] = True
articulations = []
while heap:
	_, v = heappop(heap)
	if not heap:
		articulations.append(v)
	for u in prev[v]:
		if not explored[u]:
			explored[u] = True
			heappush(heap, (-dist[u], u))

print(' '.join(map(str, sorted(articulations))))
