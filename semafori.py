N, L = map(int, input().split())
d, t = 0, 0
for _ in range(N):
	D, R, G = map(int, input().split())
	t += D - d
	d = D
	t += max(R-t%(R+G), 0)
print(t+L-d)