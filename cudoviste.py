from collections import Counter
R, C = map(int, input().split())
M = [input() for _ in range(R)]
D = {0:0, 1:0, 2:0, 3:0, 4:0}
for r in range(R-1):
	for c in range(C-1):
		p = M[r][c]+M[r][c+1]+M[r+1][c]+M[r+1][c+1]
		if '#' not in p:
			D[p.count('X')] += 1
for i in range(5):
	print(D[i])
