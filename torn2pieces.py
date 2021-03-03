from collections import deque
from itertools import islice

# bug 1: start and end could be new stations never mentioned in map
graph = {}
for _ in range(int(input())):
	stations = input().split()
	u = stations[0]
	graph.setdefault(u, set()).update(islice(stations, 1, None))
	for v in islice(stations, 1, None):
		graph.setdefault(v, set()).add(u)
start, end = input().split()
graph.setdefault(start, set())
graph.setdefault(end, set())
parent = {end: None}
queue = deque((end,))
while queue and queue[0] != start:
	u = queue.popleft()
	for v in graph[u]:
		if v not in parent:
			parent[v] = u
			queue.append(v)
if not queue:
	print("no route found")
	exit()
path = []
cur = start
while cur != None:
	path.append(cur)
	cur = parent[cur]
print(" ".join(path))
