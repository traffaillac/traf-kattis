from string import digits
from sys import stdin

D = {}
for line in stdin.read().splitlines()[:-1]:
	if '=' in line:
		k, v = line.split(" = ")
		D[k] = int(v)
	else:
		v = 0
		terms = []
		for k in line.split(" + "):
			if k[0] in digits:
				v += int(k)
			elif k in D:
				v += D[k]
			else:
				terms.append(k)
		if v != 0 or len(terms) == 0:
			terms.insert(0, str(v))
		print(" + ".join(terms))
