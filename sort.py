input()
N = [int(n) for n in input().split()]
values = {}
start = {}
for i, n in enumerate(N):
	values[n] = values.setdefault(n, 0) + 1
	start.setdefault(n, i)
values = list(values.items())
values.sort(key=lambda t: start[t[0]])
values.sort(key=lambda t: t[1], reverse=True)
for v, n in values:
	for i in range(n):
		print(v, end=' ')
print()
