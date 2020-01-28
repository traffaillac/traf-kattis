# Corner cases:
# robot going back on its track
# robot executing a last buggy instruction while on diamond
adj = ((1,0), (0,1), (-1,0), (0,-1))
board = [list(input()) for _ in range(8)]
x,y,d = 0,7,0
for i in input():
	if i == 'F':
		x += adj[d][0]
		y += adj[d][1]
		if not 0<=x<8 or not 0<=y<8 or board[y][x]=='C' or board[y][x]=='I':
			print('Bug!')
			exit()
	elif i == 'R':
		d = (d+1)&3
	elif i == 'L':
		d = (d-1)&3
	elif i == 'X':
		X,Y = x+adj[d][0],y+adj[d][1]
		if not 0<=X<8 or not 0<=Y<8 or board[Y][X]!='I':
			print('Bug!')
			exit()
		board[Y][X] = '.'
print('Diamond!' if board[y][x]=='D' else 'Bug!')
