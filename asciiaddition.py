digits = [
	'xxxxxx...xx...xx...xx...xx...xxxxxx',
	'....x....x....x....x....x....x....x',
	'xxxxx....x....xxxxxxx....x....xxxxx',
	'xxxxx....x....xxxxxx....x....xxxxxx',
	'x...xx...xx...xxxxxx....x....x....x',
	'xxxxxx....x....xxxxx....x....xxxxxx',
	'xxxxxx....x....xxxxxx...xx...xxxxxx',
	'xxxxx....x....x....x....x....x....x',
	'xxxxxx...xx...xxxxxxx...xx...xxxxxx',
	'xxxxxx...xx...xxxxxx....x....xxxxxx',
	'.......x....x..xxxxx..x....x.......']

grid = [input() for _ in range(7)]
s = []
for i in range(0,len(grid[0]),6):
	c = digits.index(''.join((grid[j][i:i+5] for j in range(7))))
	s.append(str(c) if c < 10 else '+')
res = str(eval(''.join(s)))
grid = [['.'] * (len(res)*6-1) for _ in range(7)]
for i, c in enumerate(res):
	for j in range(7):
		grid[j][i*6:i*6+5] = digits[int(c)][j*5:j*5+5]
print('\n'.join(''.join(r) for r in grid))
