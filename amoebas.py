m, n = map(int, input().split())
grid = [list(input()) for _ in range(m)]
loops = 0
for i in range(m):
	for j in range(n):
		if grid[i][j] == '.':
			continue
		r, c = i, j
		try:
			while True:
				grid[r][c] = '.'
				r, c = next((r+dr,c+dc) for dr,dc in ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)) if 0<=r+dr<m and 0<=c+dc<n and grid[r+dr][c+dc]=='#')
		except:
			loops += 1
print(loops)
