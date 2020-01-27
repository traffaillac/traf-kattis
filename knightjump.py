N = int(input())
grid = [input() for _ in range(N)]
explored = [[False] * N for _ in range(N)]
fifo = []
for r in range(N):
	for c in range(N):
		if grid[r][c] == 'K':
			fifo.append((r, c, 0))
while fifo:
	r, c, steps = fifo.pop(0)
	if not 0 <= r < N or not 0 <= c < N:
		continue
	if r == 0 and c == 0:
		print(steps)
		break
	if not explored[r][c] and grid[r][c] != '#':
		explored[r][c] = True
		fifo.append((r + 2, c + 1, steps + 1))
		fifo.append((r + 2, c - 1, steps + 1))
		fifo.append((r - 2, c + 1, steps + 1))
		fifo.append((r - 2, c - 1, steps + 1))
		fifo.append((r + 1, c + 2, steps + 1))
		fifo.append((r + 1, c - 2, steps + 1))
		fifo.append((r - 1, c + 2, steps + 1))
		fifo.append((r - 1, c - 2, steps + 1))
else:
	print(-1)
