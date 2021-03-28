cards = []
for _ in range(4):
	cards.extend(input().split())
nosets = True
for i, c in enumerate(cards):
	for j in range(i+1, len(cards)):
		d = cards[j]
		for k in range(j+1, len(cards)):
			e = cards[k]
			if (c[0]==d[0]==e[0] or c[0]!=d[0]!=e[0] and c[0]!=e[0]) and \
				(c[1]==d[1]==e[1] or c[1]!=d[1]!=e[1] and c[1]!=e[1]) and \
				(c[2]==d[2]==e[2] or c[2]!=d[2]!=e[2] and c[2]!=e[2]) and \
				(c[3]==d[3]==e[3] or c[3]!=d[3]!=e[3] and c[3]!=e[3]):
				print(i+1, j+1, k+1)
				nosets = False
if nosets:
	print("no sets")
