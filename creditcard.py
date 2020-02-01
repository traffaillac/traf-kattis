for _ in range(int(input())):
	R,B,M = (int(i) for i in input().replace('.','').split())
	for p in range(1200):
		B += (R*B+5000)//10000 - M
		if B <= 0:
			print(p+1)
			break
	else:
		print('impossible')
