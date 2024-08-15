n, m = map(int, input().split())
R = {}
for _ in range(n):
	x, _, y = input().split()
	R[x] = y
S = input()
for _ in range(m):
	S = ''.join(R.get(c, c) for c in S)
print(S)