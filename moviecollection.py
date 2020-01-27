def fenwick_add(a, i, diff):
	while i < len(a):
		a[i] += diff
		i |= i + 1
def fenwick_sum(a, i):
	s = 0
	while i >= 0:
		s += a[i]
		i = (i & i + 1) - 1
	return s



for t in range(int(input())):
	M, R = map(int, input().split())
	F = [0] * (M + R)
	P = [R + i - 1 for i in range(M + 1)]
	top = R
	for i in range(R, M + R):
		fenwick_add(F, i, 1)
	for a in map(int, input().split()):
		fenwick_add(F, P[a], -1)
		print(fenwick_sum(F, P[a]), end=' ')
		top -= 1
		P[a] = top
		fenwick_add(F, top, 1)
	print()
