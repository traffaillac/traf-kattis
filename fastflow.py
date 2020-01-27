# Capacity scaling O(E²logU) - augments paths with decreasing min capacity
# - beware of cycles in graph
# - beware of edges on same node
# - beware of multiple edges between same nodes
# - beware of need for backtracking an edge for a same delta
def maxflow(G, s, t):
	N = len(G)
	F = [[0] * N for _ in range(N)]
	flow = 0
	delta = 1 << 30 # min capacity for admissible edges
	rem = [True] * N # which nodes remain to be explored
	
	def dfs(u):
		if u == t:
			return True
		if not rem[u]:
			return False
		rem[u] = False
		for v, c in G[u].items():
			if c - F[u][v] >= delta and dfs(v):
				F[u][v] += delta
				F[v][u] -= delta
				rem[u] = True
				return True
		return False
	
	while delta > 0:
		for i in range(N):
			rem[i] = True
		if dfs(s):
			flow += delta
		else:
			delta //= 2
	return flow, F

# should solve SPOJ fastflow
N, M = map(int, input().split())
G = [{} for _ in range(N)]
for i in range(M):
	u, v, c = map(int, input().split())
	G[v - 1][u - 1] = G[u - 1][v - 1] = G[u - 1].get(v - 1, 0) + c
print(maxflow(G, 0, N - 1)[0])
