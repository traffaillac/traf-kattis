X = {'u':0,'d':0,'l':-1,'r':1}
Y = {'u':1,'d':-1,'l':0,'r':0}
while True:
	w, l = map(int, input().split())
	if w==l==0: break
	xr, yr, xa, ya = 0, 0, 0, 0
	for _ in range(int(input())):
		d, m = input().split()
		m = int(m)
		xr += X[d]*m
		yr += Y[d]*m
		xa = min(max(xa+X[d]*m, 0), w-1)
		ya = min(max(ya+Y[d]*m, 0), l-1)
	print(f"Robot thinks {xr} {yr}\nActually at {xa} {ya}\n")