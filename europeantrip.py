from math import acos, hypot, pi, sin

def main():
	xA, yA = map(int, input().split())
	xB, yB = map(int, input().split())
	xC, yC = map(int, input().split())
	xAB, yAB = xB - xA, yB - yA
	xAC, yAC = xC - xA, yC - yA
	xBC, yBC = xC - xB, yC - yB
	c = hypot(xAB, yAB)
	b = hypot(xAC, yAC)
	a = hypot(xBC, yBC)
	# compute vertices angles with dot products
	aA = acos((xAB * xAC + yAB * yAC) / c / b)
	aC = acos((xAC * xBC + yAC * yBC) / b / a)
	aB = pi - aA - aC
	if aA >= pi * 2 / 3:
		return print(xA, yA)
	if aB >= pi * 2 / 3:
		return print(xB, yB)
	if aC >= pi * 2 / 3:
		return print(xC, yC)
	# compute Fermat point by its trilinear coordinates
	x, y, z = 1/sin(aA+pi/3), 1/sin(aB+pi/3), 1/sin(aC+pi/3)
	wA, wB, wC = a*x/(a*x+b*y+c*z), b*y/(a*x+b*y+c*z), c*z/(a*x+b*y+c*z)
	print(wA*xA+wB*xB+wC*xC, wA*yA+wB*yB+wC*yC)

main()
