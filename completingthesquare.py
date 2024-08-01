x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())
x3,y3 = map(int, input().split())
if (x1-x2)*(x3-x2)+(y1-y2)*(y3-y2)==0: # angle on 2 -> swap with 1
	x1,y1,x2,y2 = x2,y2,x1,y1
if (x1-x3)*(x2-x3)+(y1-y3)*(y2-y3)==0: # angle on 3 -> swap with 1
	x1,y1,x3,y3 = x3,y3,x1,y1
print(x2+x3-x1, y2+y3-y1) # by symmetry from center point