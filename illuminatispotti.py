N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
t = 0
for i in range(N):
	for j in range(i+1, N):
		if G[i][j]:
			t += sum(G[i][k]*G[j][k] for k in range(j+1, N))
print(t)