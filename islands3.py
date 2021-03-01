R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]
islands = 0
stack = []
for r in range(R):
	for c in range(C):
		if grid[r][c] != "L": continue
		islands += 1
		stack.append((r, c))
		grid[r][c] = True # special value meaning "visited"
		while stack:
			i, j = stack.pop()
			for di,dj in ((-1,0), (0,-1), (1,0), (0,1)):
				if 0<=i+di<R and 0<=j+dj<C and (grid[i+di][j+dj]=="L" or grid[i+di][j+dj]=="C"):
					grid[i+di][j+dj] = True
					stack.append((i+di, j+dj))
print(islands)
