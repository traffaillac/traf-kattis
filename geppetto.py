N, M = map(int, input().split())
masks = []
for _ in range(M):
	a, b = (int(i)-1 for i in input().split())
	masks.append(1 << a | 1 << b)
print(sum(all(i&m!=m for m in masks) for i in range(1<<N)))
