n = int(input())
L = []
for i in range(n):
	for j, p in enumerate(map(int, input().split())):
		if p > 0:
			L.append((i+1, j+1, p))
L.sort()
print(len(L))
for i, j, p in L:
	print(i, j, p)
