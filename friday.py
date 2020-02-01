for _ in range(int(input())):
	input()
	M = [int(i) for i in input().split()]
	days = 0
	count = 0
	for d in M:
		if d>=13 and days%7 == 0:
			count += 1
		days += d
	print(count)