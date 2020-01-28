while True:
	avail = [True]*10
	while True:
		i = int(input())-1
		if i < 0: exit()
		r = input()
		if r == 'too high':
			avail[i:] = [False]*(10-i)
		elif r == 'too low':
			avail[:i+1] = [False]*(i+1)
		elif r == 'right on':
			print('Stan may be honest' if avail[i] else 'Stan is dishonest')
			break