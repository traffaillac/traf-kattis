while True:
	m = int(input())
	if m==0: break
	x, y, W, H = 0, 0, 0, 0
	while True:
		w, h = map(int, input().split())
		if w==h==-1: break
		if x+w>m:
			x, y, H = 0, H, 0
		x += w
		W = max(W, x)
		H = max(H, y+h)
	print(W, 'x', H)
