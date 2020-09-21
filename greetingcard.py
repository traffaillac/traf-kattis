points = {tuple(map(int, input().split())) for _ in range(int(input()))}
dirs = ((2018, 0), (1680, 1118), (1118, 1680),
	(0, 2018), (-1118, 1680), (-1680, 1118))
s = 0
for p in points:
	for d in dirs:
		s += (p[0]+d[0], p[1]+d[1]) in points
print(s)
