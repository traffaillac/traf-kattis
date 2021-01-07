for _ in range(int(input())):
	r, e, c = map(int, input().split())
	print('advertise' if e-c>r else 'do not advertise' if e-c<r else 'does not matter')
