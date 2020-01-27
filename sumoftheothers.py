from sys import stdin

for l in stdin:
	V = [int(v) for v in l.split()]
	S = sum(V)
	for v in V:
		if v * 2 == S:
			print(v)
			break
