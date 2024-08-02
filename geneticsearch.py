import re

def count(L, S):
	return sum(len(re.findall(f"(?={s})", L)) for s in S)

for l in open(0):
	if l[0]=='0': break
	S, L = l.split()
	D = {S[:i]+S[i+1:] for i in range(len(S))}
	I = {S[:i]+c+S[i:] for i in range(len(S)+1) for c in "ACGT"}
	print(count(L,[S]), count(L,D), count(L,I))