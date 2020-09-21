for _ in range(int(input())):
	print(input())
	addr = input()
	print(addr)
	rem = int(addr.split()[0])
	digits = [0] * 10
	while rem > 0:
		l = input().split()
		if l[0] == "+":
			for i in range(int(l[1]), int(l[2])+1, int(l[3])):
				rem -= 1
				for d in str(i):
					digits[int(d)] += 1
		else:
			rem -= 1
			for d in l[0]:
				digits[int(d)] += 1
	for i, d in enumerate(digits):
		print(f"Make {d} digit {i}")
	print(f"In total {sum(digits)} digit{'s' if sum(digits)>1 else ''}")
