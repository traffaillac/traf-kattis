from sys import stdin
for l in stdin:
	W = l.split()
	s = next(i for i,w in enumerate(W) if not w.isalpha())
	e = next(i for i in range(len(W)-1,-1,-1) if not W[i].isalpha())+1
	print(sum(map(float, W[s:e]))/(e-s), *(W[:s] if s>0 else W[e:]))