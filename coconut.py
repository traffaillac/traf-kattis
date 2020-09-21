s, n = (int(i) for i in input().split())
hands = list(range(n))
pos = 0
while len(hands) > 1:
	pos = (pos + s - 1) % len(hands)
	if hands[pos] < n:
		hands[pos] += n
		hands.insert(pos, hands[pos])
	elif hands[pos] < n * 2:
		hands[pos] += n
		pos += 1
	else:
		hands.pop(pos)
print(hands[0] % n + 1)
