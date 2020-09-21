votes = {}
while True:
	v = input()
	if v == "***": break
	votes[v] = votes.get(v, 0) + 1
m = max(votes, key=votes.__getitem__)
print(m if sum(v==votes[m] for v in votes.values())==1 else "Runoff!")
