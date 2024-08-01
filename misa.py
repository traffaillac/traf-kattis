R, S = map(int, input().split())
G = ['.'*(S+2)]+['.'+input()+'.' for _ in range(R)]+['.'*(S+2)]
h, m = 0, 0
for r in range(R):
	for s in range(S):
		p = (G[r][s:s+3]+G[r+1][s:s+3]+G[r+2][s:s+3]).count('o')
		if G[r+1][s+1] == 'o':
			h += p-1
		else:
			m = max(m, p)
print(h//2+m)