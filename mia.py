def score(a:int, b:int):
	return 72 if a+b==3 else 65+a if a==b else max(a,b)*10+min(a,b)

while True:
	s, S, r, R = (int(i) for i in input().split())
	if s==S==r==R==0: break
	print('Player 1 wins.' if score(s,S)>score(r,R) else
		'Player 2 wins.' if score(s,S)<score(r,R) else 'Tie.')
