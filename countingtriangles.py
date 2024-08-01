from itertools import *

def cross(x1,y1,x2,y2):
	return x1*y2-x2*y1

def intersect(x1,y1,X1,Y1,x2,y2,X2,Y2):
	return cross(X1-x1,Y1-y1,x2-x1,y2-y1)*cross(X1-x1,Y1-y1,X2-x1,Y2-y1)<=0 and cross(X2-x2,Y2-y2,x1-x2,y1-y2)*cross(X2-x2,Y2-y2,X1-x2,Y1-y2)<=0

def triangle(x1,y1,X1,Y1,x2,y2,X2,Y2,x3,y3,X3,Y3):
	return intersect(x1,y1,X1,Y1,x2,y2,X2,Y2) and intersect(x1,y1,X1,Y1,x3,y3,X3,Y3) and intersect(x2,y2,X2,Y2,x3,y3,X3,Y3)

while True:
	n = int(input())
	if n==0: break
	L = [[float(f) for f in input().split()] for _ in range(n)]
	print(sum(triangle(x1,y1,X1,Y1,x2,y2,X2,Y2,x3,y3,X3,Y3) for (x1,y1,X1,Y1),(x2,y2,X2,Y2),(x3,y3,X3,Y3) in combinations(L, 3)))
