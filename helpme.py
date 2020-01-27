from sys import stdin
values = {'K':0,'Q':1,'R':2,'B':3,'N':4}
board = stdin.read().split()
white = []
black = []
for r in range(8):
	for c in range(8):
		p = board[2*r+1][4*c+2]
		if p.isupper():
			white.append(f'{p if p!="P" else ""}{chr(97+c)}{8-r}')
		elif p.islower():
			black.append(f'{p.upper() if p!="p" else ""}{chr(97+c)}{8-r}')
white.sort(key=lambda s:(values[s[0]] if len(s)>2 else 5,s[-1],s[-2]))
black.sort(key=lambda s:(values[s[0]] if len(s)>2 else 5,8-int(s[-1]),s[-2]))
print('White:', ','.join(white))
print('Black:', ','.join(black))
