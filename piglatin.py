for L in open(0):
	W = []
	for w in L.split():
		if w[0] in "aeiouy":
			W.append(w+"yay")
		else:
			i = next(i for i, c in enumerate(w) if c in "aeiouy")
			W.append(w[i:]+w[:i]+"ay")
	print(' '.join(W))