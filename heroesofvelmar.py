def power(C, iscenter):
	P = {"Shadow":6, "Gale":5, "Ranger":4, "Anvil":7, "Vexia":3, "Guardian":8, "Thunderheart":6, "Frostwhisper":2, "Voidclaw":3, "Ironwood":3, "Zenith":4, "Seraphina":1}
	p = sum(P[c] for c in C)
	if len(C)==4:
		p += C.count("Thunderheart")*6
	if iscenter:
		p += C.count("Zenith")*5
	p += C.count("Seraphina")*(len(C)-1)
	return p

l1 = power(input().split()[1:], False)
l2 = power(input().split()[1:], False)
c1 = power(input().split()[1:], True)
c2 = power(input().split()[1:], True)
r1 = power(input().split()[1:], False)
r2 = power(input().split()[1:], False)
loc1 = (l1>l2)+(c1>c2)+(r1>r2)
loc2 = (l2>l1)+(c2>c1)+(r2>r1)
print("Player 1" if loc1>loc2 or loc1==loc2 and l1+c1+r1>l2+c2+r2 else
      "Player 2" if loc2>loc1 or loc2==loc1 and l2+c2+r2>l1+c1+r1 else "Tie")