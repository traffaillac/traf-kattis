for t in range(int(input())):
	S = input()
	N = [[1]*(len(S)+1)]+[[0]*(len(S)+1) for _ in "welcome to code jam"]
	for r, x in enumerate("welcome to code jam"):
		for c, s in enumerate(S):
			N[r+1][c+1] = (N[r+1][c] + (N[r][c] if x==s else 0)) % 10000
	print(f"Case #{t+1}: {N[-1][-1]:04d}")