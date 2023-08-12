def cross(x0, y0, x1, y1, x, y):
	return abs((x1-x0)*(y-y0)-(x-x0)*(y1-y0))
xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())
a = abs(xa*(yb-yc)+xb*(yc-ya)+xc*(ya-yb))
print(f"{a/2:.1f}")
c = 0
for _ in range(int(input())):
	x, y = map(int, input().split())
	if cross(xa,ya,xb,yb,x,y) + cross(xb,yb,xc,yc,x,y) + cross(xc,yc,xa,ya,x,y) == a:
			c += 1
print(c)