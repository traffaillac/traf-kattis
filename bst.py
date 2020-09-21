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


N = int(input())
parent = [0] * (N+1)
range_left = [0] * N
range_right = [N-1] * N
depth = [0] * N
root = int(input()) - 1
fenwick_add(parent, 0, root)
C = 0
print(0)
for _ in range(N-1):
	i = int(input()) - 1
	p = fenwick_sum(parent, i)
	depth[i] = depth[p] + 1
	C += depth[i]
	print(C)
	if i < p:
		fenwick_add(parent, range_left[p], i-p)
		fenwick_add(parent, p, p-i)
		range_left[i] = range_left[p]
		range_right[i] = p-1
		range_left[p] = p
	else:
		fenwick_add(parent, p+1, i-p)
		fenwick_add(parent, range_right[p]+1, p-i)
		range_left[i] = p+1
		range_right[i] = range_right[p]
		range_right[p] = p
