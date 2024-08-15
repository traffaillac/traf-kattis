N = int(input())
P = [tuple(map(float, input().split())) for _ in range(N)]
A = int(input())
f = (A*2/sum(x*Y-y*X for (x,y),(X,Y) in zip(P,P[1:]+P[:1])))**.5
mx, my = min(x for x,y in P), min(y for x,y in P)
for x,y in P:
	print((x-mx)*f, (y-my)*f)