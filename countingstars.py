from sys import setrecursionlimit
setrecursionlimit(10002) # tested with 100x100 full star

def dfs(grid, m, n, r, c):
	grid[r][c] = '#'
	for i,j in ((-1,0), (0,-1), (1,0), (0,1)):
		if 0<=r+i<m and 0<=c+j<n and grid[r+i][c+j] == '-':
			dfs(grid, m, n, r+i, c+j)

for t in range(1, 51):
	try: m, n = map(int, input().split())
	except: break
	grid = [list(input()) for _ in range(m)]
	stars = 0
	for r in range(m):
		for c in range(n):
			if grid[r][c] == '-':
				stars += 1
				dfs(grid, m, n, r, c)
	print("Case %d: %d" % (t, stars))
