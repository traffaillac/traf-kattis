P = int(input())
for p in range(P):
	K, i = input().split()
	try:
		o = int(i, 8)
	except:
		o = 0
	print(K, o, int(i, 10), int(i, 16))
