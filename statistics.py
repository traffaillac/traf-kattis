for t in range(10):
	try:
		X = [int(i) for i in input().split()[1:]]
	except: break
	print(f'Case {t+1}: {min(X)} {max(X)} {max(X)-min(X)}')
