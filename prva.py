R, C = map(int, input().split())
G = [input() for _ in range(R)]
W = []
for L in G:
	for w in L.split('#'):
		if len(w)>=2:
			W.append(w)
for c in range(C):
	for w in ''.join(G[r][c] for r in range(R)).split('#'):
		if len(w)>=2:
			W.append(w)
W.sort()
print(W[0])