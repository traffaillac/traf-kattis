for _ in range(int(input())):
	s,d = (int(i) for i in input().split())
	a,b = (s+d)//2, (s-d)//2
	print(f'{a} {b}' if b>=0 and s&1==d&1 else 'impossible')
