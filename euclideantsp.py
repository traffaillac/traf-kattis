from math import log2

n, p, s, v = map(float, input().split())
f = lambda c:n*log2(n)**(c*2**.5)/p/1000000000+s*(1+1/c)/v
a, b, c = 0.000001, 50, 100
while c-a>0.000001:
	d, e = (a+b)/2, (b+c)/2
	if f(b)>=f(e)<=f(c):
		a, b, c = b, e, c
	elif f(d)>=f(b)<=f(e):
		a, b, c = d, b, e
	else:
		a, b, c = a, d, b
print(f(b), b)