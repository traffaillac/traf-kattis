adj = ((-1, 0), (0, -1), (0, 1), (1, 0))
n, m = (int(i) for i in input().split())
tree = [input() for _ in range(n)]
rings = [[0] * len(t) for t in tree]
bfs = []
for r in range(n):
	for c in range(m):
		if tree[r][c]=='T' and (r==0 or r==n-1 or c==0 or c==m-1 or any(tree[r+dr][c+dc]=='.' for dr,dc in adj)):
			rings[r][c] = 1
			bfs.append((r, c))
while bfs:
	r, c = bfs.pop(0)
	for dr,dc in adj:
		if 0<=r+dr<n and 0<=c+dc<m and tree[r+dr][c+dc]=='T' and rings[r+dr][c+dc]==0:
			rings[r+dr][c+dc] = rings[r][c] + 1
			bfs.append((r+dr, c+dc))
width = "2" if rings[r][c] < 10 else "3"
for ring in rings:
	print("".join((f"{r:.>{width}}" if r>0 else "."*int(width)) for r in ring))
