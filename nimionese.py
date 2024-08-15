F = "BBCDDGGGGKKKNNNPPPTTTTTTTT      bbcddggggkkknnnppptttttttt"
W = []
for w in input().split():
	if w[0].lower() not in "bcdgknpt":
		w = F[ord(w[0])-ord('A')]+w[1:]
	w = ''.join(''.join(c if i==0 or c not in "bcdgknpt" else w[0].lower() for c in s) for i,s in enumerate(w.split('-')))
	if w[-1].lower() in "bcdgknpt":
		w += "ah" if w[-1].lower() in "bcdg" else "oh" if w[-1].lower() in "knp" else "uh"
	W.append(w)
print(' '.join(W))