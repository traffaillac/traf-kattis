s, *G = open(0)
s = int(s)
W = set()
while len(W)<4:
	s = s+s//13+15
	W.add((s//10%10,s%10))
for g in G:
	x, y = map(int, g[:2])
	if (x, y) in W:
		print("You hit a wumpus!")
		W.remove((x, y))
	if W:
		print(min(abs(x-a)+abs(y-b) for a, b in W))
print(f"Your score is {len(G)} moves.")