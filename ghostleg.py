n, m = map(int, input().split())
p = list(range(1, n+1))
for _ in range(m):
	a = int(input())-1
	p[a], p[a+1] = p[a+1], p[a]
for i in p:
	print(i)
