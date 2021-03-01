R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]
stack = []
area = 0
for r in range(R):
	for c in range(C):
		g = grid[r][c]
		if g!="0" and g!="1": continue
		stack.append((r, c))
		area += int(g)
		grid[r][c] = area
		while stack:
			i, j = stack.pop()
			for di,dj in ((-1,0), (0,-1), (1,0), (0,1)):
				if 0<=i+di<R and 0<=j+dj<C and grid[i+di][j+dj]==g:
					grid[i+di][j+dj] = area
					stack.append((i+di, j+dj))
		area = (area & -2) + 2

for _ in range(int(input())):
	r1, c1, r2, c2 = (int(i)-1 for i in input().split())
	print("neither" if grid[r1][c1] != grid[r2][c2] else "decimal" if grid[r1][c1]&1 else "binary")
