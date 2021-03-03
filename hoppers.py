N, M = map(int, input().split())
graph = [[] for _ in range(N)]
colors = [None] * N
for _ in range(M):
	u, v = (int(i)-1 for i in input().split())
	graph[u].append(v)
	graph[v].append(u)
stack = []
components = 0
bipartite = True
for n in range(N):
	if colors[n] is None:
		colors[n] = 0
		components += 1
		stack.append(n)
		while stack:
			u = stack.pop()
			for v in graph[u]:
				if colors[v] == colors[u]:
					bipartite = False
				elif colors[v] is None:
					colors[v] = colors[u] ^ 1
					stack.append(v)
print(components if bipartite else components-1)
