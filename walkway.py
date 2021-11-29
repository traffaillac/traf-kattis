from pprint import pprint
from heapq import heappush, heappop

while True:
	n = int(input())
	if n == 0: break
	graph = {}
	for _ in range(n):
		a, b, h = map(int, input().split())
		cost = (a + b) * h
		graph.setdefault(a, []).append((b, cost))
		graph.setdefault(b, []).append((a, cost))
	
	start, end = map(int, input().split())
	visited = set()
	fifo = [(0, start)]
	while fifo[0][1] != end:
		total, a = heappop(fifo)
		if a in visited: continue
		visited.add(a)
		for b, cost in graph[a]:
			if b not in visited:
				heappush(fifo, (total + cost, b))
	print("%.2f" % (fifo[0][0] / 100))
