N = int(input())
a = [0] * N
for _ in range(N):
	for i, m in enumerate(input().split()):
		a[i] |= int(m)
print(*a)
