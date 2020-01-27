from heapq import heappush, heappop
from math import hypot

def set_find(s, i):
	while s[i] >= 0:
		i = s[i]
	return i
def set_union(s, i, j):
	i = set_find(s, i)
	j = set_find(s, j)
	if i != j:
		if -s[i] < -s[j]:
			i, j = j, i
		s[i] += s[j]
		s[j] = i

N = int(input())
for n in range(N):
	S, P = map(int, input().split())
	coords = [tuple(int(i) for i in input().split()) for p in range(P)]
	heap = [(0.0, 0)]
	distmin = [20000.0] * P
	links = []
	while heap:
		d, p = heappop(heap)
		if distmin[p] != 0.0:
			distmin[p] = 0.0
			links.append(d)
			for q in range(P):
				if distmin[q] != 0.0:
					d = hypot(coords[p][0] - coords[q][0], coords[p][1] - coords[q][1])
					if distmin[q] > d:
						distmin[q] = d
						heappush(heap, (d, q))
	links.sort()
	print('%.2f'%links[-S])
