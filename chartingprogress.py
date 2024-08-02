for S in open(0).read().split("\n\n"):
	G = S.split()
	V = sorted((next(r for r, g in enumerate(G) if g[c]=='*') for c in range(len(G[0]))), reverse=True)
	for r in range(len(G)):
		print(''.join(".*"[V[c]==r] for c in range(len(G[0]))))
	print()