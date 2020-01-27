dyns = []
for m in range(3, 101):
	dyn = [1] * 10001
	p = m
	while p <= 10000:
		for i in range(p, 10001):
			dyn[i] += dyn[i - p]
		p *= m
	dyns.append(dyn)

P = int(input())
for _ in range(P):
	K, m, n = map(int, input().split())
	print(K, dyns[m - 3][n])
