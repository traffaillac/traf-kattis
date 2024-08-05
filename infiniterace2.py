N, _, *E = map(int, open(0))
behind = set()
cross = 0
for e in E:
	if e < 0:
		behind.discard(-e)
	elif e in behind:
		behind = {e}
		cross += 1
	else:
		behind.add(e)
print(cross)