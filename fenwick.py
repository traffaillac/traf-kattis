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

N, Q = map(int, stdin.readline().split())
a = [0] * N
for _ in range(Q):
	op = stdin.readline().split()
	if op[0] == '+':
		fenwick_add(a, int(op[1]), int(op[2]))
	else:
		print(fenwick_sum(a, int(op[1])-1))
