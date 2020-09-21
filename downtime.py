# Fenwick tree (on array initialized with 0)
def fenwick_add(a:list, i:int, diff:int):
	while i < len(a):
		a[i] += diff
		i |= i + 1
def fenwick_sum(a:list, i:int):
	s = 0
	while i >= 0:
		s += a[i]
		i = (i & (i + 1)) - 1
	return s

n, k = (int(i) for i in input().split())
a = [0] * 101_001
for i in range(n):
	t = int(input())
	fenwick_add(a, t, 1)
	fenwick_add(a, t+1000, -1)
print((max(fenwick_sum(a, i) for i in range(100_001))+k-1) // k)
