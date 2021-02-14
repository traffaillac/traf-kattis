def dfs(graph, visited, u):
	visited[u] = True
	for v in graph[u]:
		if not visited[v]:
			dfs(graph, visited, v)

for _ in range(int(input())):
	m = int(input())
	graph = [[] for i in range(m)]
	for _ in range(int(input())):
		u, v = map(int, input().split())
		graph[u].append(v)
		graph[v].append(u)
	visited = [False] * m
	components = 0
	for u in range(m):
		if not visited[u]:
			components += 1
			dfs(graph, visited, u)
	print(components - 1)
