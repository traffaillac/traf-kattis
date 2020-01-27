while True:
	a, b, c, d = (int(i) for i in input().split())
	if a==b==c==d==0: break
	deg = 720
	deg += (a-b)%40*9
	deg += 360
	deg += (c-b)%40*9
	deg += (c-d)%40*9
	print(deg)
