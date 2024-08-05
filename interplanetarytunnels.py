from collections import deque

n, m = map(int, input().split())
pa, pb = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
	u, v = map(int, input().split())
	G[u].append(v)
	G[v].append(u)
V = {pa:0}
Q = deque([pa])
while True:
	u = Q.popleft()
	for v in G[u]:
		if v==pb:
			print(V[u]//2+1)
			exit()
		if v not in V:
			V[v] = V[u] + 1
			Q.append(v)