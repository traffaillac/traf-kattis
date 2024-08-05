from math import *

while True:
	a, b, s, m, n = map(int, input().split())
	if a==0: break
	print(f"{atan2(b*n,a*m)*180/pi:.2f} {hypot(b*n,a*m)/s:.2f}")