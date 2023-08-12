n, m = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(n)]
l = 1_000_000_000
for r in range(n):
	for c in range(m):
		l = min(l, sum(G[i][j]*(abs(i-r)+abs(j-c)) for i in range(n) for j in range(m)))
print(l)