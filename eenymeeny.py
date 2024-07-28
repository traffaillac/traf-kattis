r = len(input().split())-1
K = [input() for _ in range(int(input()))]
i, t, T = 0, 0, [[], []]
while K:
	i = (i+r)%len(K)
	T[t].append(K.pop(i))
	t ^= 1
for t in T:
	print(len(t))
	print('\n'.join(t))
