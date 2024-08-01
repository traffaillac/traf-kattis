C = ["#."*10,".#"*10]
M, N = map(int, input().split())
U, L, R, D = map(int, input().split())
P = [input() for _ in range(M)]
for r in range(U):
	print(C[r%2][:L+N+R])
for r in range(M):
	print(C[(U+r)%2][:L]+P[r]+C[(U+r)%2][L+N:L+N+R])
for r in range(D):
	print(C[(U+M+r)%2][:L+N+R])
