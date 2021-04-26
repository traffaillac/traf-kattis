P, K = map(int, input().split())
piles = [[int(i) for i in input().split()[1:]] for _ in range(P)]
grundy = [[0] for _ in range(P)]
xor = 0
for p, g in zip(piles, grundy):
	for n in range(1, len(p)+1): # number of cards remaining on p
		children = set(g[n-k-p[n-k-1]] for k in range(min(K+1, n)) if p[n-k-1]<=n-k)
		g.append(next(i for i in range(12) if i not in children))
	xor ^= g[-1]
print("Alice can win." if xor else "Bob will win.")
