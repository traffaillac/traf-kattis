n, _ = map(int, input().split())
K = [set([int(i) for i in input().split()][1:]) for _ in range(n)]
S = [0] * n
for l in map(int, input().split()):
	m = min(*S)
	for i in range(n):
		S[i] = min(S[i], m+1) if l in K[i] else 1000
print(min(*S))
