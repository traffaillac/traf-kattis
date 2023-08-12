N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]
fifo = [(r,c) for r in range(N) for c in range(M) if grid[r][c]=='V']
while fifo:
	r, c = fifo.pop()
	if r == N-1 or grid[r+1][c] == 'V':
		pass
	elif grid[r+1][c] == '.':
		grid[r+1][c] = 'V'
		fifo.append((r+1, c))
	elif grid[r+1][c] == '#':
		if c > 0 and grid[r][c-1] == '.':
			grid[r][c-1] = 'V'
			fifo.append((r, c-1))
		if c < M-1 and grid[r][c+1] == '.':
			grid[r][c+1] = 'V'
			fifo.append((r, c+1))
for line in grid:
	print(''.join(line))
