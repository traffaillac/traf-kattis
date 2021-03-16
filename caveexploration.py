import sys
sys.setrecursionlimit(10010)

# graph is a list/dict of adjacency lists, depth and low are None-initialized arrays
def dfs(graph, depth, low, i, d=0, parent=None):
	count = 1
	depth[i] = low[i] = d
	for j in graph[i]:
		if depth[j] is None:
			child = dfs(graph, depth, low, j, d+1, i)
			if low[j] <= d:
				count += child
			low[i] = min(low[i], low[j])
		elif j != parent:
			low[i] = min(low[i], depth[j])
	return count

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)
print(dfs(graph, [None]*N, [None]*N, 0))
