for _ in range(int(input())):
	m, p = map(int, input().split())
	orders = [tuple(map(int, input().split())) for _ in range(m)]
	orders.sort(key=lambda t:t[1])
	avail = [p, p, p, p, p, 0, 0] * 15
	try:
		for b, e in orders:
			i = next(i for i in range(b, e+1) if avail[i] >= 2)
			avail[i] -= 2
	except:
		try:
			avail = [p, p, p, p, p, p, p] * 15
			for b, e in orders:
				i = next(i for i in range(b, e+1) if avail[i] >= 2)
				avail[i] -= 2
		except:
			print('serious trouble')
		else:
			print('weekend work')
	else:
		print('fine')
