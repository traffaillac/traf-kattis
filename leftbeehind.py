while True:
	x, y = (int(i) for i in input().split())
	if x==y==0: break
	print('Never speak again.' if x+y==13 else 'Left beehind.' if y>x else 'To the convention.' if x>y else 'Undecided.')