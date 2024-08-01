n, s = map(int, input().split())
t = s
r = 0
for _ in range(n):
	c = input()
	x = int(c[0]) + (len(c)==2)
	if t<x:
		t = s
		r += 1
	t -= x
print(r)