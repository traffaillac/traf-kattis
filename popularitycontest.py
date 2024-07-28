N, M = map(int, input().split())
F = [0]*N
for _ in range(M):
	a, b = map(int, input().split())
	F[a-1] += 1
	F[b-1] += 1
print(*(f-i-1 for i, f in enumerate(F)))