from bisect import bisect_left

R = [r*r for r in range(20,220,20)]
for _ in range(int(input())):
	S = 0
	for _ in range(int(input())):
		x, y = map(int, input().split())
		S += 10 - bisect_left(R, x*x+y*y)
	print(S)