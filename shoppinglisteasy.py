n, m = map(int, input().split())
items = set.intersection(*(set(input().split()) for _ in range(n)))
print(len(items))
for i in sorted(items):
	print(i)
