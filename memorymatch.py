N = int(input())
cards = [None]*N
for _ in range(int(input())):
	C1,C2,P1,P2 = input().split()
	C1,C2 = int(C1)-1,int(C2)-1
	cards[C1] = P1
	cards[C2] = P2
	if P1 == P2:
		cards[C1] = cards[C2] = False
seen = {}
for c in cards:
	if c: seen[c] = seen.get(c,0) + 1
singles = list(seen.values()).count(1)
doubles = list(seen.values()).count(2)
hidden = cards.count(None)
print(doubles+singles if hidden==singles else doubles+1 if hidden==2 else doubles)
