from heapq import heappop, heappush

N, M = map(int, input().split())
A, B, K, _ = map(int, input().split())
I = list(map(int, input().split()))
G = [{} for _ in range(N+1)]
for _ in range(M):
	a, b, l = map(int, input().split())
	G[a][b] = G[b][a] = [l, 0, 0]
t = 0
for a, b in zip(I, I[1:]):
	L = G[a][b]
	L[1] = t
	t += L[0]
	L[2] = t
H = [(K,A)]
V = {A:K}
while H[0][1]!=B:
	t, u = heappop(H)
	if t > V[u]: continue
	for v, (l, c, o) in G[u].items():
		tv = o+l if c<=t<o else t+l
		if v not in V or V[v]>tv:
			V[v] = tv
			heappush(H, (tv, v))
print(H[0][0]-K)