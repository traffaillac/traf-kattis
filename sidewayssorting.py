while True:
	r, c = (int(i) for i in input().split())
	if r == c == 0: break
	T = [input() for _ in range(r)]
	T = ["".join(T[i][j] for i in range(r)) for j in range(c)]
	T.sort(key=str.casefold)
	T = ["".join(T[i][j] for i in range(c)) for j in range(r)]
	print("\n".join(T))
	print()