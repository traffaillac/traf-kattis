F = " - - - - -   -"
G = ["GFEDCBAgfedcba",':'*14]
input()
S = ' '*14
for n in input().split():
	p = n[0]
	d = 1 if p==n else int(n[1:])
	i = G[0].index(p)
	G.append(S)
	S = F
	G.extend([F[:i]+'*'+F[i+1:]]*d)
print('\n'.join(''.join(g[i] for g in G) for i in range(14)))