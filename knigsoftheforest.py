from heapq import heappush, heappop
from sys import stdin

k, n = map(int, stdin.readline().split())
mooses = [tuple(map(int, stdin.readline().split())) for _ in range(n+k-1)]
karl = -mooses[0][1]
heap = []
for y, p in sorted(mooses):
	heappush(heap, -p)
	if len(heap) == k and heappop(heap) == karl:
		print(y)
		break
else:
	print("unknown")
