from heapq import *

n = int(input())
D = [[int(d) for d in input().split()] for _ in range(n)]
visited = {0}
avail = {v:D[0][v] for v in range(1,n)}
H = [(D[0][v],0,v) for v in range(1,n)]
heapify(H)
while avail:
	_,u,v = heappop(H)
	if v in visited: continue
	del avail[v]
	visited.add(v)
	print(u+1, v+1)
	for w,d in avail.items():
		if d>D[v][w]:
			avail[w] = d = D[v][w]
			heappush(H, (d,v,w))
