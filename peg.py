G = [input() for _ in range(7)]
for c in range(7):
	G.append(''.join(G[r][c] for r in range(7)))
print(sum(l.count("oo.")+l.count(".oo") for l in G))