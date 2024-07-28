a, b, c, l = map(int, input().split())
im = True
for i in range(l//a+1):
	for j in range((l-i*a)//b+1):
		if (l-i*a-j*b)%c==0:
			print(i, j, (l-i*a-j*b)//c)
			im = False
if im:
	print("impossible")