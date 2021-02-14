def dfs(graph, visited, x):
	visited[x] = True
	for y in graph[x]:
		if not visited[y]:
			dfs(graph, visited, y)

for _ in range(int(input())):
	n, m, l = map(int, input().split())
	graph = [[] for i in range(n)]
	for i in range(m):
		x, y = (int(i)-1 for i in input().split())
		graph[x].append(y)
	visited = [False] * n
	for i in range(l):
		dfs(graph, visited, int(input())-1)
	print(sum(visited))
