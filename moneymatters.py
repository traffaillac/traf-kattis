n, m = map(int, input().split())
balance = [int(input()) for _ in range(n)]
graph = [[] for _ in range(n)]
for _ in range(m):
	x, y = map(int, input().split())
	graph[x].append(y)
	graph[y].append(x)
queued = [False] * n
for start in range(n):
	if not queued[start]:
		fifo = [start]
		queued[start] = True
		total = 0
		while fifo:
			x = fifo.pop()
			total += balance[x]
			for y in graph[x]:
				if not queued[y]:
					fifo.append(y)
					queued[y] = True
		if total != 0:
			print("IMPOSSIBLE")
			break
else:
	print("POSSIBLE")
