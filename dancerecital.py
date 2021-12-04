from heapq import heapify, heappush, heappop
from itertools import product

R = int(input())
routines = [input() for _ in range(R)]
changes = [[None] * R for _ in range(R)]
for (i, r), (j, q) in product(enumerate(routines), repeat=2):
	changes[i][j] = changes[j][i] = len(set(r) & set(q))
heap = [(0, i, 1<<i) for i in range(R)]
min_changes = {(i, 1<<i): 0 for i in range(R)}
while heap[0][2] != (1<<R)-1:
	c, i, m = heappop(heap)
	if c > min_changes[(i, m)]:
		continue
	for j in range(R):
		n = m | 1<<j
		d = c + changes[i][j]
		if n != m and d < min_changes.get((j, n), 1000):
			min_changes[j, n] = d
			heappush(heap, (d, j, n))
print(heap[0][0])
