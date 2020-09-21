board = [input() for _ in range(5)]
def valid(r:int, c:int):
	if board[r][c] == ".":
		return False
	for dr, dc in ((-1,-2), (-2,-1), (-2,1), (-1,2), (1,-2), (2,-1), (2,1), (1,2)):
		if 0<=r+dr<5 and 0<=c+dc<5 and board[r+dr][c+dc]=="k":
			return False
	return True
print("valid" if sum(valid(r, c) for r in range(5) for c in range(5))==9 else "invalid")
