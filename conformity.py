combinations = {}
for _ in range(int(input())):
	cs = tuple(sorted(map(int, input().split())))
	combinations[cs] = combinations.get(cs, 0) + 1
m = max(combinations.values())
print(sum(p for p in combinations.values() if p == m))
