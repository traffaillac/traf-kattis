while True:
	try:
		M, P, L, E, R, S, N = (int(i) for i in input().split())
	except: break
	for n in range(N):
		M, P, L = P//S, L//R, M*E
	print(M)
