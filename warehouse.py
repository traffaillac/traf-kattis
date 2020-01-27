from operator import itemgetter

for t in range(int(input())):
	toys = {}
	for n in range(int(input())):
		name, num = input().split()
		toys[name] = toys.setdefault(name, 0) + int(num)
	items = sorted(toys.items(), key=lambda t: t[0])
	items.sort(key=lambda t: t[1], reverse=True)
	print(len(items))
	for i in items:
		print(i[0], i[1])
