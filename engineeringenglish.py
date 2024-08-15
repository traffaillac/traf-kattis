D = set()
for l in open(0):
	W = []
	for w in l.split():
		if w.lower() in D:
			W.append('.')
		else:
			D.add(w.lower())
			W.append(w)
	print(' '.join(W))
