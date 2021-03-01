# adding a water border around the map makes the problem MUCH easier
R, C = (int(i)+2 for i in input().split())
grid = [["0"]*C] + [list("0"+input()+"0") for _ in range(R-2)] + [["0"]*C]
stack = [(0, 0)]
grid[0][0] = True # special value meaning "visited"
coast = 0
while stack:
	r, c = stack.pop()
	for dr,dc in ((-1,0), (0,-1), (1,0), (0,1)):
		if 0<=r+dr<R and 0<=c+dc<C:
			if grid[r+dr][c+dc] == "0":
				grid[r+dr][c+dc] = True
				stack.append((r+dr, c+dc))
			elif grid[r+dr][c+dc] == "1":
				coast += 1
print(coast)
