from sys import stdin

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

N, K = map(int, stdin.readline().split())
bits = [-1] * N
sums = [0] * N
for _ in range(K):
	op, *args = stdin.readline().split()
	if op == 'F':
		i = int(args[0]) - 1
		bits[i] *= -1
		fenwick_add(sums, i, bits[i])
	else:
		l, r = (int(i)-1 for i in args)
		print(fenwick_sum(sums, r) - fenwick_sum(sums, l-1))
