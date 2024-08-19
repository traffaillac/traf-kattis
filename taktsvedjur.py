r, m, s = 0, 1, 0
for _ in range(int(input())):
	x = int(input())
	r = min(r+1,8) if x else 0
	if r==m*2:
		r, m = 0, r
	elif x==0:
		m = max(m//2,1)
	s += x*m
print(s)