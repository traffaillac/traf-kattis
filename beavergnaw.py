from math import pi
while True:
	D, V = map(int, input().split())
	if D==V==0: break
	print((6/pi*(pi*D**3/6-V))**(1/3))