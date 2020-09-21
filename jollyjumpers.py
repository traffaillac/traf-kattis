while True:
	try: _, *a = (int(i) for i in input().split())
	except: break
	present = [False]*(len(a)-1)
	for i in range(len(a)-1):
		d = abs(a[i]-a[i+1])
		if 1 <= d <= len(a)-1:
			present[d-1] = True
	print("Jolly" if len(a)==1 or all(present) else "Not jolly")
