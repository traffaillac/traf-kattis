for t in range(int(input())):
	input()
	input()
	g = max(int(i) for i in input().split())
	m = max(int(i) for i in input().split())
	print('Godzilla' if g>=m else 'MechaGodzilla')
