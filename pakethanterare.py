t, b = map(int, input().split())
T = list(map(int, input().split()))
V = {}
for _ in range(t):
	n, v = input().split()
	V[n] = int(v)
for i, ti in enumerate(T):
	s = 0
	for _ in range(ti):
		n, v = input().split()
		s += V[n]-int(v)
	print(s)
