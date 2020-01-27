from math import sin, cos
p, a, b, c, d, n = (int(i) for i in input().split())
top, dec = 0, 0
for k in range(1, n+1):
	price = p*(sin(a*k+b)+cos(c*k+d)+2)
	dec = max(dec, top-price)
	top = max(top, price)
print(dec)
