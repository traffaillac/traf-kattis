from itertools import product

N, M = map(int, input().split())
counts = [0] * (N + M - 1)
for i, j in product(range(N), range(M)):
	counts[i+j] += 1
best = max(counts)
for s, c in enumerate(counts):
	if c == best:
		print(2 + s)
