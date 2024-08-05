n = int(input())
V = {chr(ord('A')+i):(c=='T') for i, c in enumerate(input().split())}
S = []
for c in input().split():
	if c in V:
		S.append(V[c])
	elif c=='*':
		S.append(S.pop() & S.pop())
	elif c=='+':
		S.append(S.pop() | S.pop())
	elif c=='-':
		S[-1] = not S[-1]
print("FT"[S[-1]])