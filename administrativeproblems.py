for _ in range(int(input())):
	n, m = map(int, input().split())
	cars = {}
	for _ in range(n):
		name, p, q, k = input().split()
		cars[name] = (int(p), int(q), int(k))
	spies = {}
	for _ in range(m):
		t, S, e, C = input().split()
		spies.setdefault(S, []).append((int(t), e, C))
	for S, events in sorted(spies.items()):
		driving = None
		cost = 0
		for t, e, C in events:
			if e == "p":
				if driving != None: break
				cost += cars[C][1]
				driving = C
			elif e == "r":
				if driving == None: break
				cost += int(C) * cars[driving][2]
				driving = None
			elif e == "a":
				if driving == None: break
				cost += (cars[driving][0] * int(C) + 99) // 100
		else:
			if driving == None:
				print(S, cost)
				continue
		print(S, "INCONSISTENT")
