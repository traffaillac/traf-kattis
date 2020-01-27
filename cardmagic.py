N, K, T = (int(x) for x in input().split())
W = [0] * (T + 1)
S = [0] * (T + 1)
for t in range(1, min(K, T) + 1):
	W[t] = 1
for n in range(1, N):
	sum = 0
	for t in range(T):
		sum = (sum + W[t]) % 1_000_000_009
		S[t + 1] = sum
	for t in range(1, T + 1):
		W[t] = (S[t] - S[max(0, t - K)] + 1_000_000_009) % 1_000_000_009
print(W[T])
