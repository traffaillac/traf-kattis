for _ in range(int(input())):
	C = "abcdefgh"
	P = input()
	S = [(8-int(P[1]), C.index(P[0]))]
	i = -1
	m = 0
	while len(S)<64:
		m += 1
		for i in range(i+1, len(S)):
			r, c = S[i]
			for dr in (-2, -1, 1, 2):
				for dc in (abs(dr)^3, -(abs(dr)^3)):
					if 0<=r+dr<8 and 0<=c+dc<8 and (r+dr, c+dc) not in S:
						S.append((r+dr, c+dc))
	print(m, *(C[c]+str(8-r) for r, c in sorted(S[i+1:])))