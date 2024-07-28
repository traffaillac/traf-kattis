from heapq import heappop, heappush

n, m = map(int, input().split())
G = [{} for _ in range(n)]
for _ in range(m):
	a, b, c = map(int, input().split())
	G[a-1][b-1] = G[b-1][a-1] = c
H = [(0,0)]
V = {0:0}
while H and H[0][1]!=n-1:
	b, u = heappop(H)
	if b!=V[u]: continue
	for v, c in G[u].items():
		if v not in V or V[v]>b+c:
			V[v] = b+c
			heappush(H, (b+c,v))
print(H[0][0])
