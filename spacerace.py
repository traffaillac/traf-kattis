n = int(input())
d = float(input())
E, N = 0, ''
for _ in range(n):
	name, _, f = input().split()
	e = d/float(f)
	if e > E:
		E, N = e, name
print(N)