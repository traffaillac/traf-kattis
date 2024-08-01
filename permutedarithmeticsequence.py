A = lambda L: all(b-a==L[1]-L[0] for a, b in zip(L,L[1:]))
for _ in range(int(input())):
	S = list(map(int, input().split()[1:]))
	print("arithmetic" if A(S) else "permuted arithmetic" if A(sorted(S)) else "non-arithmetic")