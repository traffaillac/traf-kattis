H, *path = input().split()
H = int(H)
if not path:
	print(2 ** (H + 1) - 1)
else:
	path = path[0]
	left = sum(2**i for i in range(H, len(path)-1, -1))
	print(left - int(path.replace('L', '0').replace('R', '1'), 2))
