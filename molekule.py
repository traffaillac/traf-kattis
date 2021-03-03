N = int(input())
edges = [tuple(int(i)-1 for i in input().split()) for _ in range(N-1)]
graph = [[] for _ in range(N)]
for a, b in edges:
	graph[a].append(b)
	graph[b].append(a)
colors = [None] * N
colors[0] = 0
stack = [0]
while stack:
	a = stack.pop()
	for b in graph[a]:
		if colors[b] == None:
			colors[b] = colors[a] ^ 1
			stack.append(b)
for a, _ in edges:
	print(colors[a])
