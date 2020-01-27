for _ in range(int(input())):
	Xc,Xr,Yc,Yr = input().split()
	Xc,Xr,Yc,Yr = ord(Xc)-65,int(Xr)-1,ord(Yc)-65,int(Yr)-1
	if (Xc^Xr^Yc^Yr)%2 == 1:
		print('Impossible')
	elif Xc==Yc and Xr==Yr:
		print(0, chr(65+Xc), Xr+1)
	elif abs(Xc-Yc) == abs(Xr-Yr):
		print(1, chr(65+Xc), Xr+1, chr(65+Yc), Yr+1)
	else:
		for dc,dr in ((-1,-1),(1,-1),(-1,1),(1,1)):
			Zc,Zr = Xc,Xr
			for i in range(7):
				Zc += dc
				Zr += dr
				if 0<=Zc<8 and 0<=Zr<8 and abs(Zc-Yc)==abs(Zr-Yr): break
			else: continue
			break
		print(2, chr(65+Xc), Xr+1, chr(65+Zc), Zr+1, chr(65+Yc), Yr+1)
