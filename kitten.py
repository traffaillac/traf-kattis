G = [0]*101
K = [int(input())]
while True:
	a, *B = map(int, input().split())
	if a<0: break
	for b in B:
		G[b] = a
while G[K[-1]]>0:
	K.append(G[K[-1]])
print(*K)