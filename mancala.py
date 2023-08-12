# Golfed afterwards though not kept ;)
B = [0] * 80
W = []
for N in range(2000):
	b = B.index(0)
	B[b] = b+1
	for i in range(b):
		B[i] -= 1
	l = next(i for i in range(79, -1, -1) if B[i]>0)
	W.append(B[:l+1])
for _ in range(int(input())):
	K, N = map(int, input().split())
	w = W[N-1]
	print(K, len(w))
	for i in range(0, len(w), 10):
		print(*w[i:i+10])