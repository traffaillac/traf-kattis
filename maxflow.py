# Capacity scaling O(E²logU) - augments paths with decreasing min capacity
# - beware of cycles in graph
# - beware of edges on same node
# - beware of multiple edges between same nodes
# - beware of need for unpushing an edge for a same delta
import sys
sys.setrecursionlimit(5000)

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

# should solve Kattis maxflow
n, m, s, t = map(int, input().split())
G = [{} for _ in range(n)]
for i in range(m):
	u, v, c = map(int, input().split())
	G[u][v] = G[u].get(v, 0) + c
f, F = maxflow(G, s, t)
print(n, f, sum(F[u][v] > 0 for u in range(n) for v in range(n)))
for u in range(n):
	for v in range(n):
		if F[u][v] > 0:
			assert F[u][v] <= G[u][v] and F[v][u] == -F[u][v]
			print(u, v, F[u][v])
