for _ in range(int(input())):
	n, m = (int(i) for i in input().split())
	prizes = []
	for i in range(n):
		*types, cash = (int(i) for i in input().split()[1:])
		prizes.append((types, cash))
	stickers = [int(i) for i in input().split()]
	total = 0
	for types,cash in prizes:
		total += cash*min(stickers[t-1] for t in types)
	print(total)
