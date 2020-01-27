for n in range(int(input())):
	name, *items = (input() for k in range(int(input())+1))
	if 'pea soup' in items and 'pancakes' in items:
		print(name)
		break
else:
	print('Anywhere is fine I guess')
