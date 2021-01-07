N = int(input())
l = input().split()
t0, v0 = int(l[0]), float(l[1])
area = 0.0
for _ in range(N - 1):
	l = input().split()
	t1, v1 = int(l[0]), float(l[1])
	area += (t1 - t0) * (v0 + v1) / 2 / 1000
	t0, v0 = t1, v1
print(area)
