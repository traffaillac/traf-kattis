C = input()
W = input().split()
D = {}
E = {}
for c, w in zip(C, W):
	if D.get(c, w)!=w or E.get(w, c)!=c:
		print(False)
		exit()
	D[c] = w
	E[w] = c
print(len(C)==len(W))