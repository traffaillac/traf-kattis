n, k = (int(i) for i in input().split())
pos = [0]
it = iter(input().split())
for c in it:
	if c == "undo":
		pos = pos[:-int(next(it))]
	else:
		pos.append((pos[-1] + int(c)) % n)
print(pos[-1])
