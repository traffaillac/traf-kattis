N, Q = map(int, input().split())
X = list(map(int, input().split()))
for _ in range(Q):
	q, a, b = map(int, input().split())
	if q == 1:
		X[a-1] = b
	else:
		print(abs(X[a-1] - X[b-1]))
