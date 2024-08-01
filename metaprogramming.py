V = {}
for s in open(0):
	a, b, c, *d = s.split()
	if a=="define":
		V[c] = int(b)
	elif b not in V or d[0] not in V:
		print("undefined")
	else:
		b, d = V[b], V[d[0]]
		print("true" if c=='<' and b<d or c=='=' and b==d or c=='>' and b>d else "false")