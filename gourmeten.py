M = int(input())
N = int(input())
T = [int(input()) for _ in range(N)]
ways = [0] * (M+1)
ways[0] = 1
for m in range(M):
	for t in T:
		if m+t<=M:
			ways[m+t] += ways[m]
print(ways[M])