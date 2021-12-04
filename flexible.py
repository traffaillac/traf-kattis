W, _ = map(int, input().split())
P = [0] + [int(p) for p in input().split()] + [W]
widths = set()
for i in range(len(P) - 1):
	for j in range(i+1, len(P)):
		widths.add(P[j] - P[i])
print(' '.join(map(str, sorted(widths))))
