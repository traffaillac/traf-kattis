from heapq import heappush, heappop
from sys import stdin

def main():
	M, N = map(int, next(stdin).split())
	piles = [[int(p) for p in next(stdin).split()] for _ in range(M)]
	heap = [(0, 0, 0)]
	visited = [[False] * N for _ in range(M)]
	while heap:
		h, m, n = heappop(heap)
		if not visited[m][n]:
			visited[m][n] = True
			if m == M - 1 and n == N - 1:
				break
			for dm, dn in ((-1,0), (1,0), (0,-1), (0,1)):
				mm, nn = m + dm, n + dn
				if 0 <= mm < M and 0 <= nn < N and not visited[mm][nn]:
					hh = max(h, piles[mm][nn] - piles[m][n])
					heappush(heap, (hh, mm, nn))
	print(h)
main()
