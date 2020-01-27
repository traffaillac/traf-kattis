from string import digits, ascii_letters
from sys import stdin

dots = digits+ascii_letters
for img in stdin.read().rstrip().split('\n\n'):
	grid = [list(l) for l in img.split()]
	try:
		r,c = next((r,c) for r in range(len(grid)) for c in range(len(grid[r])) if grid[r][c]=='0')
		target = '1'
		while True:
			try: R,C = next((r,i) for i in range(len(grid[r])) if grid[r][i]==target)
			except: R,C = next((i,c) for i in range(len(grid)) if grid[i][c]==target)
			dr,dc = (R>r)-(R<r), (C>c)-(C<c)
			while r!=R or c!=C:
				if dr == 0 and not grid[r][c] in dots and grid[r][c] != '-':
					grid[r][c] = '-' if grid[r][c] == '.' else '+'
				if dc == 0 and not grid[r][c] in dots and grid[r][c] != '|':
					grid[r][c] = '|' if grid[r][c] == '.' else '+'
				r += dr
				c += dc
			target = dots[dots.index(target)+1]
	except: pass
	print('\n'.join(''.join(l) for l in grid))
	print()
