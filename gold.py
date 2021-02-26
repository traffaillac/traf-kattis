import sys
sys.setrecursionlimit(2308) # value obtained from 50x50 biggest area

def dfs(grid, r, c):
	gold = 1 if grid[r][c] == 'G' else 0
	grid[r][c] = ' ' # mark this cell visited
	if all(grid[r+i][c+j] != 'T' for i,j in ((-1,0), (0,-1), (1,0), (0,1))):
		for i,j in ((-1,0), (0,-1), (1,0), (0,1)):
			if grid[r+i][c+j] == '.' or grid[r+i][c+j] == 'G':
				gold += dfs(grid, r+i, c+j)
	return gold

W, H = map(int, input().split())
grid = [list(input()) for _ in range(H)]
r, c = next((r, c) for r in range(H) for c in range(W) if grid[r][c] == 'P')
print(dfs(grid, r, c))
