n = int(input())
K = [0]+[*map(int, input().split())]
V = [False] * (n+1)
r = 0
for i in range(1, n+1):
	if V[i] or K[i]==i: continue
	s = 0
	j = i
	while not V[j]:
		V[j] = True
		s += 1
		j = K[j]
	r += s+1
print(r)