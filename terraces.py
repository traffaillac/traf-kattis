# Bug 1: Recursion limit exceeded
# Bug 2: Increasing recursion limit results in memory limit exceeded
# Bug 3: Nodes were added multiple times before flagged visited
X, Y = map(int, input().split())
garden = [[int(i) for i in input().split()] for _ in range(Y)]
visited = [[False] * X for _ in range(Y)]
area = 0
for R in range(Y):
	for C in range(X):
		if not visited[R][C]:
			visited[R][C] = True
			size = 0
			closed = True
			stack = [(R, C)]
			while stack:
				r, c = stack.pop()
				size += 1
				for y, x in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)):
					if 0<=y<len(garden) and 0<=x<len(garden[y]):
						if garden[y][x] < garden[r][c]:
							closed = False
						elif garden[y][x] == garden[r][c] and not visited[y][x]:
							stack.append((y, x))
							visited[y][x] = True
			if closed:
				area += size
print(area)
