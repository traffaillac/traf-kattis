while True:
	try:
		n,k = (int(i) for i in input().split())
	except: break
	wins = [0]*n
	losses = [0]*n
	for _ in range(k*n*(n-1)//2):
		p1,m1,p2,m2 = input().split()
		if m1=='rock' and m2=='scissors' or m1=='scissors' and m2=='paper' or m1=='paper' and m2=='rock':
			wins[int(p1)-1] += 1
			losses[int(p2)-1] += 1
		elif m2=='rock' and m1=='scissors' or m2=='scissors' and m1=='paper' or m2=='paper' and m1=='rock':
			wins[int(p2)-1] += 1
			losses[int(p1)-1] += 1
	for w,l in zip(wins,losses):
		print(f'{w/(w+l):.3f}' if w+l>0 else '-')
	print()