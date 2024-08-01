for _ in range(int(input())):
	print(sum(int(d or 0)*60**i for i, d in enumerate(input().split(',')[::-1])))