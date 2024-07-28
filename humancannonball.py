from math import hypot
P = [tuple(map(float, input().split())), tuple(map(float, input().split()))]
for _ in range(int(input())):
	P.append(tuple(map(float, input().split())))
M = [[0]*len(P) for _ in range(len(P))]
for i, (x, y) in enumerate(P):
	for j in range(i, len(P)):
		d = hypot(x-P[j][0], y-P[j][1])
		M[i][j] = M[j][i] = d/5 if i==0 else (d-50)/5+2 if d>50 else min(d/5, 2+(50-d)/5)
for k in range(len(P)):
	for i in range(len(P)):
		for j in range(len(P)):
			M[i][j] = min(M[i][j], M[i][k]+M[k][j])
print(M[0][1])