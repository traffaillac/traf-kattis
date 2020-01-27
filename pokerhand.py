counts = {}
for c in input().split():
	counts[c[0]] = counts.get(c[0],0) + 1
print(max(counts.values()))
