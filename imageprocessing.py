H, W, N, M = (int(i) for i in input().split())
image = [[int(i) for i in input().split()] for _ in range(H)]
kernel = [[int(i) for i in input().split()] for _ in range(N)]
col = [0] * (W-M+1)
for r in range(H-N+1):
	for c in range(W-M+1):
		col[c] = sum(image[r+i][c+j]*kernel[-1-i][-1-j] for i in range(N) for j in range(M))
	print(" ".join(map(str, col)))
