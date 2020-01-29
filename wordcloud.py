from math import ceil

for t in range(20):
	W,N = (int(i) for i in input().split())
	if W==N==0: break
	C = [input().split() for _ in range(N)]
	C = [(len(w),int(c)) for w,c in sorted(C) if int(c)>=5]
	cmax = max(c for _,c in C)
	w,h,H = 0,0,0
	for l,c in C:
		p = 8+ceil(40*(c-4)/(cmax-4))
		width = ceil(9/16*l*p)
		if w+width > W:
			H += h
			h = 0
			w = 0
		w += width+10
		h = max(h, p)
	print(f'CLOUD {t+1}: {H+h}')
