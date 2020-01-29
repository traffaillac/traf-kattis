for _ in range(int(input())):
	n = input()
	s = 0
	for i in range(len(n)):
		s += int(n[-1-i]) if i%2==0 else sum(int(c) for c in str(int(n[-1-i])*2))
	print('PASS' if s%10==0 else 'FAIL')
