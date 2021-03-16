# graph is a list/dict of adjacency lists, depth and low are None-initialized arrays
def articulation_bridges(graph, depth, low, i, d=0, parent=None, res=None):
	if res is None:
		res = []
	depth[i] = low[i] = d
	for j in graph[i]:
		if depth[j] is None:
			articulation_bridges(graph, depth, low, j, d+1, i, res)
			if low[j] > d:
				res.append((i, j))
			low[i] = min(low[i], low[j])
		elif j != parent:
			low[i] = min(low[i], depth[j])
	return res

while True:
	p, c = map(int, input().split())
	if p == 0: break
	graph = [[] for _ in range(p)]
	for _ in range(c):
		a, b = map(int, input().split())
		graph[a].append(b)
		graph[b].append(a)
	depth = [None] * p
	print('Yes' if articulation_bridges(graph, depth, [None]*p, 0) or None in depth else 'No')
		