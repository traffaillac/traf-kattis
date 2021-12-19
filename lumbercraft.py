from itertools import product

while True:
	n, h, w = map(int, input().split())
	if n == 0: break
	grid = [list(input()) for _ in range(h)]
	players = {}
	trees = {}
	scores = {}
	for r, c in product(range(h), range(w)):
		p = grid[r][c]
		if p != '!' and p != '.':
			players[p] = (r, c)
			trees[p] = []
			scores[p] = 0
	for r, c in product(range(h), range(w)):
		if grid[r][c] == '!':
			for p, (pr, pc) in players.items():
				trees[p].append(((r-pr)**2+(c-pc)**2, -c, -r))
	for t in trees.values():
		t.sort(reverse=True)
	for _ in range(n):
		cuts = {}
		for p, t in trees.items():
			while t:
				_, c, r = t.pop()
				if grid[-r][-c] == '!':
					cuts.setdefault((-r, -c), []).append(p)
					break
		for (r, c), lumbers in cuts.items():
			grid[r][c] = '.'
			for p in lumbers:
				scores[p] += 1 / len(lumbers)
	
	print('\n'.join(''.join(line) for line in grid))
	for p, s in sorted(scores.items()):
		print(p, s)
