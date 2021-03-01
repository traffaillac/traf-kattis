# Bug 1: Forgot to initialise node L as visited
# Bug 2: stack.pop(0) triggered a TLE
C, P, X, L = map(int, input().split())
countries = [[] for _ in range(C)]
for _ in range(P):
	A, B = (int(i)-1 for i in input().split())
	countries[A].append(B)
	countries[B].append(A)
stack = [L-1]
nb = [0] * C # number of leavers in neighbours
nb[L-1] = False
while stack:
	c = stack.pop()
	if c == X-1:
		print("leave")
		exit()
	for d in countries[c]:
		if nb[d] is False: continue
		nb[d] += 1
		if nb[d]*2 >= len(countries[d]):
			stack.append(d)
			nb[d] = False # special value meaning "left the union"
print("stay")
