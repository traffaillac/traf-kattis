def kills(G, K, r, c):
	return sum(G[i].count('*', c+1, c+K-1) for i in range(r+1,r+K-1))
R, S, K = map(int, input().split())
G = [input() for _ in range(R)]
m, rk, ck = max((kills(G,K,r,c),r,c) for r in range(R-K+1) for c in range(S-K+1))
print(m)
for r, g in enumerate(G):
	if rk<=r<=rk+K-1:
		print(g[:ck] + ('|'+g[ck+1:ck+K-1]+'|' if rk<r<rk+K-1 else '+'+'-'*(K-2)+'+') + g[ck+K:])
	else:
		print(g)