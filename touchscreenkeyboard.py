def dist(a, b):
	layout = 'qwertyuiopasdfghjklzxcvbnm'
	ia = layout.index(a)
	ib = layout.index(b)
	ra = ia // 10 if ia < 19 else 2
	rb = ib // 10 if ib < 19 else 2
	ca = ia % 10 if ia < 19 else ia - 19
	cb = ib % 10 if ib < 19 else ib - 19
	return abs(ra - rb) + abs(ca - cb)

def distword(a, b):
	sum = 0
	for c, d in zip(a, b):
		sum += dist(c, d)
	return sum

for t in range(int(input())):
	s, l = input().split()
	words = []
	for i in range(int(l)):
		w = input()
		words.append((w, distword(s, w)))
	words.sort()
	words.sort(key=lambda t: t[1])
	for t in words:
		print(t[0], t[1])
