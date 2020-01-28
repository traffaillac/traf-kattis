# Shooting at same coordinate twice
# Second player shooting to win after being destroyed
# Hitting the last ship of an enemy (and not playing again)
# Fake shot orders after end of game
# End of orders during a turn (NOT EXPLICITED)
for _ in range(int(input())):
	w,h,n = (int(i) for i in input().split())
	maps = ([list(input()) for _ in range(h)], [list(input()) for _ in range(h)])
	rem = [sum(l.count('#') for l in maps[i]) for i in range(2)]
	order = 0
	while order<n and rem[0]>0 and rem[1]>0:
		for player in range(2):
			while order < n:
				x,y = (int(i) for i in input().split())
				order += 1
				# print(f'player {player} shoots {x},{y} -> {"hit" if maps[player^1][y][x] == "#" else "miss"}')
				if maps[player^1][h-1-y][x] == '_': break
				maps[player^1][h-1-y][x] = '_'
				rem[player^1] -= 1
				if rem[player^1] == 0: break
	for i in range(order,n):
		input()
	print('player one wins' if rem[0]>0 and rem[1]==0 else
		'player two wins' if rem[0]==0 and rem[1]>0 else 'draw')
