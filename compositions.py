mem = {}
def compositions(n, m, k):
	if n == 0:
		return 1
	if n in mem:
		return mem[n]
	c = sum(compositions(n-i, m, k) for i in range(1, n+1) if i<m or (i-m)%k!=0)
	mem[n] = c
	return c

for _ in range(int(input())):
	mem.clear()
	K, n, m, k = map(int, input().split())
	print(K, compositions(n, m, k))
